from django.contrib import admin

# Register your models here.
from shop.db_models.purchases_db_model import Purchases
from shop.db_models.shop_item_db_model import ShopItem

admin.site.register(ShopItem)
admin.site.register(Purchases)
