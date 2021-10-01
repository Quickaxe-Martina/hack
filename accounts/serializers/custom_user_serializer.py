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
    faculty = FacultySerializer()

    class Meta:
        model = CustomUser
        fields = [
            'id', 'username', 'first_name', 'last_name', 'middle_name',
            'email', 'faculty', 'avatar', 'y_coin',
        ]
        read_only_fields = ['id',]
