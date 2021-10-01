from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.db_models.answer_db_model import Answer
from core.serializers.answer_serializer import AnswerSerializer
from django.shortcuts import get_object_or_404



class AnswerListView(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post']
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('question', 'author',)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        q = Answer.objects.create(**serializer.validated_data, author=request.user)
        return Response(data=self.get_serializer(q).data, status=201)


class AnswerDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'put']

    def get(self, request, pk):
        answer = get_object_or_404(Answer, pk=pk)
        return Response(data=AnswerSerializer(answer).data)

    def put(self, request, pk):
        answer = get_object_or_404(Answer, pk=pk, author=request.user)

        serializer = AnswerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        answer.text = serializer.validated_data['text']
        answer.save()
        return Response(data=AnswerSerializer(answer).data)
