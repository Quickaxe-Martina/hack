from rest_framework import serializers

from core.db_models.topic_db_model import Topic


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'
        read_only_fields = ['id',]
