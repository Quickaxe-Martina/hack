from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from shop.db_models.shop_item_db_model import ShopItem
from shop.serializers.shop_item_serializer import ShopItemSerializer


class ShopItemListView(generics.ListAPIView):
    queryset = ShopItem.objects.all()
    serializer_class = ShopItemSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('name',)
