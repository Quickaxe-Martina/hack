from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters

from core.db_models.topic_db_model import Topic
from core.serializers.topic_serializer import TopicSerializer


class TopicListView(generics.ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('subject', 'name')
