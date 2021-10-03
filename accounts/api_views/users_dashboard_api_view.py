from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.db_models.question_db_model import Question


class UserDashboardAPIView(APIView):
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']

    def get(self, request):
        return Response(
            data={
                'given': Question.objects.filter(author=request.user).count(),
                'solved': Question.objects.filter(
                    answers__author=request.user, status='closed',
                    answers__user_grade__gt=0
                ).count()
            }
        )
