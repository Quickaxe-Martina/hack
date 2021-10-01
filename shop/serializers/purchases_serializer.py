from rest_framework import serializers

from shop.db_models.purchases_db_model import Purchases


class PurchasesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Purchases
        fields = '__all__'
