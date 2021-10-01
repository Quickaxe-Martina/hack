from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.db_models.likes_db_model import Like
from core.serializers.like_serializer import LikeSerializer


class LikeAPIView(APIView):
    permission_classes = [IsAuthenticated]
    http_method_names = ['post']

    def post(self, request):
        serializer = LikeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Like.objects.update_or_create(
            author=request.user, answer=serializer.validated_data['answer'],
            defaults={
                'type': serializer.validated_data['type']
            }
        )
        return Response(status=201)
