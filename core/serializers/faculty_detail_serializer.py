from rest_framework import serializers

from accounts.serializers.custom_user_serializer import CustomUserSerializer
from core.db_models.faculty_db_model import Faculty


class FacultyDetailSerializer(serializers.ModelSerializer):
    users = CustomUserSerializer(read_only=True, many=True)

    class Meta:
        model = Faculty
        fields = ['id', 'name', 'score', 'users']
        read_only_fields = ['id', 'users']
