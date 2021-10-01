from rest_framework import serializers

from accounts.serializers.custom_user_serializer import CustomUserSerializer
from core.db_models.question_db_model import Question
from core.serializers.answer_serializer import AnswerDetailSerializer


class QuestionSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'topic', 'text', 'prise', 'deadline', 'exigent', 'author']
        read_only_fields = ['id' 'author']


class QuestionDetailSerializer(serializers.ModelSerializer):
    answers_list = AnswerDetailSerializer(many=True, default=[])
    author = CustomUserSerializer(read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'topic', 'text', 'prise', 'deadline', 'exigent', 'answers_list', 'author']
        read_only_fields = ['id', 'answers_list', 'author']
