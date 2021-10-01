from rest_framework import serializers

from core.db_models.likes_db_model import Like


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'answer', 'type',]
        read_only_fields = ['id',]
