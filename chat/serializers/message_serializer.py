from rest_framework import serializers

from accounts.serializers.custom_user_serializer import CustomUserSerializer
from chat.db_models.message_db_model import MessageChat


class MessageChatSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)

    class Meta:
        model = MessageChat
        fields = '__all__'
