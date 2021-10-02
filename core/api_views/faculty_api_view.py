from django.db.models import Prefetch
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from accounts.models import CustomUser
from core.db_models.faculty_db_model import Faculty
from core.serializers.faculty_detail_serializer import FacultyDetailSerializer
from core.serializers.faculty_serializer import FacultySerializer


class FacultyListView(generics.ListAPIView):
    serializer_class = FacultyDetailSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']

    def get_queryset(self):
        return Faculty.objects.all().prefetch_related(
            Prefetch(
                'custom_users',
                queryset=CustomUser.objects.all().order_by('-faculty_count'),
                to_attr='users'
            )
        )


class FacultyRetrieveView(generics.RetrieveAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']
