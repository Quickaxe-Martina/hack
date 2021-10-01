from rest_framework import serializers

from shop.db_models.shop_item_db_model import ShopItem


class ShopItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShopItem
        fields = '__all__'
