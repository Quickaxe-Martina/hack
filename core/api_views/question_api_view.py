from django.db.models import Prefetch, Sum, Q
from django.shortcuts import get_object_or_404
from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.db_models.answer_db_model import Answer
from core.db_models.question_db_model import Question
from core.serializers.answer_serializer import AnswerCloseQuestionSerializer
from core.serializers.question_serializer import QuestionSerializer, QuestionDetailSerializer
from core.tools.update_dict import update_from_dict


class QuestionListView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionDetailSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post']
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('topic__subject', 'topic', 'status', 'author')

    def create(self, request, *args, **kwargs):
        serializer = QuestionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if request.user.y_coin <= serializer.validated_data['prise']:
            return Response(status=403, data='Тебе не хватает монет')
        q = Question.objects.create(**serializer.validated_data, author=request.user)
        request.user.y_coin -= serializer.validated_data['prise']
        request.user.save()
        return Response(data=self.get_serializer(q).data, status=201)


class QuestionDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'put', 'post']

    def get(self, request, pk):
        q = Question.objects.filter(pk=pk).prefetch_related(
            Prefetch(
                f'answers',
                queryset=Answer.objects.annotate(rating=Sum('likes__type')).order_by('-rating'),
                to_attr='answers_list'
            )
        ).first()

        return Response(data=QuestionDetailSerializer(q).data)

    def put(self, request, pk):
        q = get_object_or_404(Question, pk=pk, author=request.user, status='in_progress')

        serializer = QuestionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if q.prise != serializer.validated_data['prise']:
            request.user.y_coin += q.prise - serializer.validated_data['prise']
            request.user.save()

        update_from_dict(q, serializer.validated_data, commit=True)

        return Response(status=200)

    def post(self, request, pk):
        """ close question """

        q = get_object_or_404(Question, pk=pk, author=request.user, status='in_progress')
        serializer = AnswerCloseQuestionSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)

        map_answers = {a['id']: a['user_grade'] for a in serializer.validated_data}
        answers = Answer.objects.filter(~Q(author=request.user), pk__in=map_answers.keys())

        y_coin = q.prise * 4 / answers.count()
        for a in answers:
            a.user_grade = map_answers[a.pk]
            a.author.y_coin += y_coin
            a.author.save()
        Answer.objects.bulk_update(answers, ['user_grade'])

        q.status = 'closed'
        q.save()
        return Response(data=serializer.validated_data)
