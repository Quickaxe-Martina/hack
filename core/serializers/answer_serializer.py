from rest_framework import serializers

from accounts.serializers.custom_user_serializer import CustomUserSerializer
from core.db_models.answer_db_model import Answer


class AnswerDetailSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(allow_null=True, read_only=True)
    author = CustomUserSerializer(read_only=True)

    class Meta:
        model = Answer
        fields = '__all__'
        read_only_fields = ['id', 'rating']


class AnswerSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)

    class Meta:
        model = Answer
        fields = '__all__'
        read_only_fields = ['id', 'author', 'created']


class AnswerCloseQuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField(min_value=1)
    user_grade = serializers.IntegerField(min_value=0, max_value=5)
