from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from chat.db_models.chat_db_model import Chat, ThroughUserChat
from chat.serializers.chat_serializer import ChatSerializer, ChatDetailSerializer
from core.serializers.answer_serializer import AnswerCloseQuestionSerializer


class ChatAPIView(APIView):
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post']

    def get(self, request):
        qs = Chat.objects.filter(through_chat__user=request.user).select_related('question')
        return Response(data=ChatDetailSerializer(qs, many=True).data)

    def post(self, request):
        serializer = ChatSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        question = serializer.validated_data.get('question')

        chat = Chat.objects.create(
            type_chat=serializer.validated_data['type_chat'],
            question=question
        )

        users_list = []
        for usr in serializer.validated_data['users_list']:
            users_list.append(
                ThroughUserChat(
                    chat=chat,
                    user_id=usr,
                    is_organizer=usr == request.user.pk
                )
            )
        try:
            ThroughUserChat.objects.bulk_create(users_list)
        except Exception:
            return Response(status=400)
        return Response(data=ChatDetailSerializer(chat).data, status=201)


class ChatDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post']

    def post(self, request, pk):
        """ Закрыть чат """
        chat = get_object_or_404(Chat, pk=pk, question__status='in_progress', question__author=request.user)
        serializer = AnswerCloseQuestionSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)

        map_answers = {a['id']: a['user_grade'] for a in serializer.validated_data}
        users = ThroughUserChat.objects.filter(~Q(user=request.user), user_id__in=map_answers.keys())

        q = chat.question
        y_coin = q.prise * 4 / users.count()
        for usr in users:
            usr.user_grade = map_answers[usr.pk]
            user = usr.user
            user.add_coins(y_coin)
            user.add_exp(map_answers[usr.pk] * 30)
            user.add_faculty_count(map_answers[usr.pk])
        ThroughUserChat.objects.bulk_update(users, ['user_grade'])

        q.status = 'closed'
        q.save()
        return Response()
