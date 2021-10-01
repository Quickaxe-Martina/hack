from rest_framework import serializers


class UserAvatarSerializer(serializers.Serializer):
    avatar = serializers.ImageField()
