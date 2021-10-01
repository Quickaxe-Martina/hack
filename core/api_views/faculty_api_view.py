from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from core.db_models.faculty_db_model import Faculty
from core.serializers.faculty_serializer import FacultySerializer


class FacultyListView(generics.ListAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']
