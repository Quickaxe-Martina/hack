from rest_framework import serializers

from achievements.db_models.achievement_db_model import Achievement


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'
        read_only_fields = ['id',]
