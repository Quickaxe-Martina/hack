from django.db.models import Count
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import CustomUser
from accounts.serializers.custom_user_serializer import RegisterSerializer, CustomUserSerializer
from core.db_models.faculty_db_model import Faculty


class RegisterAPIView(APIView):
    http_method_names = ['post']

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            r_id = int(request.query_params.get('referral'))
            r_user = CustomUser.objects.get(pk=r_id)
        except Exception:
            r_user = None

        user = CustomUser.objects.create_user(**serializer.validated_data, referral=r_user)
        faculty = Faculty.objects.annotate(
            user_count=Count('custom_users')
        ).order_by(
            'user_count'
        ).first()
        user.faculty = faculty
        user.save()
        if r_user:
            r_user.add_coins(20)
        return Response(status=201, data=CustomUserSerializer(user).data)
