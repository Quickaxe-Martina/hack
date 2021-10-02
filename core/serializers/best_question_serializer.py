from rest_framework import serializers


class BestQuestionSerializer(serializers.Serializer):
    text = serializers.CharField()
