from django.db import models


class ShopItem(models.Model):

    name = models.CharField(max_length=100, verbose_name='Имя')
    image = models.ImageField(
        upload_to='shop_items', blank=True, null=True, verbose_name='Фото'
    )
    Y_coins = models.PositiveIntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = 'Товар магазина'
        verbose_name_plural = 'Товары магазина'
