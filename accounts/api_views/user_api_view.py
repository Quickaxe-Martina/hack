from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from accounts.models import CustomUser
from accounts.serializers.custom_user_serializer import CustomUserSerializer


class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']


class UserDetailView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
