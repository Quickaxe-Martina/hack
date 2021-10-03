from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from rest_framework.response import Response
from rest_framework.views import APIView

from core.db_models.topic_db_model import Topic
from rest_framework.filters import SearchFilter

from core.serializers.best_question_serializer import BestQuestionSerializer
from core.serializers.topic_serializer import TopicSerializer
from core.tools.model_class import AIModel


class TopicListView(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post']
    filter_backends = (filters.DjangoFilterBackend, SearchFilter)
    filterset_fields = ('subject',)
    search_fields = ['name',]


class BestTopicAPIView(APIView):
    permission_classes = [IsAuthenticated]
    http_method_names = ['post']

    def post(self, request):
        serializer = BestQuestionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        best = AIModel().get_close_questions(serializer.data['text'])

        return Response(TopicSerializer([b.topic for b in best], many=True).data)
