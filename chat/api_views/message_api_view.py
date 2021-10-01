from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from chat.db_models.message_db_model import MessageChat
from chat.serializers.message_serializer import MessageChatSerializer
from core.tools.message_sender import user_send_to_ws


class MessageChatListCreateView(generics.ListCreateAPIView):
    queryset = MessageChat.objects.all()
    serializer_class = MessageChatSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post']
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('chat', 'author',)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if request.user not in serializer.validated_data['chat'].users.all():
            return Response(status=403, data='Тебя нет в этом чате')
        q = MessageChat.objects.create(**serializer.validated_data, author=request.user)
        for usr in serializer.validated_data['chat'].users.all():
            user_send_to_ws(usr, {'new_message': str(serializer.validated_data['chat'].pk)})
        return Response(data=self.get_serializer(q).data, status=201)
