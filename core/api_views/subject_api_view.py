from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from core.db_models.subject_db_model import Subject
from core.serializers.subject_serializer import SubjectSerializer


class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']
