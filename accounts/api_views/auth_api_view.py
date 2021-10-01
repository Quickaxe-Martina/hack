from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import CustomUser
from accounts.serializers.custom_user_serializer import CustomUserSerializer, UserAuthSerializer


class UserAuthAPIView(APIView):
    http_method_names = ['post']

    def post(self, request):
        serializer = UserAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = get_object_or_404(CustomUser, username=serializer.validated_data['username'])
        if not user.check_password(serializer.validated_data['password']):
            return Response(status=400, data='Неверный пароль')
        token, _ = Token.objects.get_or_create(user=user)

        return Response(data={
            'token': token.key,
            **CustomUserSerializer(user).data
        })
