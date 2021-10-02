from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from achievements.db_models.achievement_db_model import Achievement
from achievements.serializers.achievement_serializer import AchievementSerializer


class AchievementListView(generics.ListAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']


class AchievementRetrieveView(generics.RetrieveAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']
