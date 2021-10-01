from rest_framework import serializers

from accounts.serializers.custom_user_serializer import CustomUserSerializer
from chat.db_models.chat_db_model import Chat, ThroughUserChat
from core.serializers.question_serializer import QuestionSerializer


class ThroughUserChatSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = ThroughUserChat
        fields = '__all__'


class ChatSerializer(serializers.ModelSerializer):
    users_list = serializers.ListSerializer(child=serializers.IntegerField(min_value=1), default=[])

    class Meta:
        model = Chat
        fields = ['id', 'created', 'type_chat', 'question', 'users_list']
        read_only_fields = ['id', 'created']


class ChatDetailSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(read_only=True)
    users = ThroughUserChatSerializer(source='through_chat', many=True)

    class Meta:
        model = Chat
        fields = ['id', 'created', 'type_chat', 'question', 'users']
        read_only_fields = ['id', 'created']
