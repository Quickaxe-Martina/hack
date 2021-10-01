from rest_framework import serializers

from accounts.models import CustomUser
from core.serializers.faculty_serializer import FacultySerializer


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'first_name', 'last_name', 'middle_name',]


class UserAuthSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class CustomUserSerializer(serializers.ModelSerializer):
    faculty = FacultySerializer(read_only=True)

    class Meta:
        model = CustomUser
        fields = [
            'id', 'username', 'first_name', 'last_name', 'middle_name',
            'email', 'faculty', 'avatar', 'y_coin', 'faculty_count', 'level', 'exp_count'
        ]
        read_only_fields = ['id',]
