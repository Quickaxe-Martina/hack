import os
import uuid

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.serializers.avatar_serializer import UserAvatarSerializer
from accounts.serializers.custom_user_serializer import CustomUserSerializer


class UserAvatarAPIView(APIView):
    http_method_names = ['post']
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = UserAvatarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        image = serializer.validated_data.get('avatar')
        try:
            type_file = os.path.splitext(image.name)[1]
            request.user.avatar.save(str(uuid.uuid4()) + type_file, image)
            return Response(status=201, data=CustomUserSerializer(request.user, context={'request': request}).data)
        except Exception as e:
            return Response(status=400, data=e)
