from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from shop.db_models.purchases_db_model import Purchases
from shop.serializers.purchases_serializer import PurchasesSerializer


class PurchasesListView(generics.ListCreateAPIView):
    serializer_class = PurchasesSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post']
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('shop_item', 'status')

    def get_queryset(self):
        return Purchases.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        shop_item = serializer.validated_data['shop_item']
        if request.user.y_coin < shop_item.y_coin:
            return Response(status=403, data='Тебе не хватает монет')
        request.user.y_coin -= shop_item.y_coin
        request.user.save()
        q = Purchases.objects.create(
            shop_item=shop_item,
            user=request.user
        )
        return Response(data=self.get_serializer(q).data, status=201)
