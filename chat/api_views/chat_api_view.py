from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from chat.db_models.chat_db_model import Chat, ThroughUserChat
from chat.serializers.chat_serializer import ChatSerializer, ChatDetailSerializer


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
