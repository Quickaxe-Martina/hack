from django.db import models

from accounts.models import CustomUser
from shop.db_models.shop_item_db_model import ShopItem


class Purchases(models.Model):

    class Status(models.TextChoices):
        IN_WORK = 'in_work', 'В работе'
        HANDED_OVER_TO_DELIVERY = 'handed_over_to_delivery', 'Передано в доставку'
        AWAITING_RECEIPT = 'awaiting_receipt', 'Ожидает получения'
        RECEIVED = 'received', 'Получено'

    shop_item = models.ForeignKey(
        ShopItem, on_delete=models.CASCADE, related_name='purchases',
        verbose_name='Товар'
    )
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='purchases',
        verbose_name='Пользователь'
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    status = models.CharField(
        max_length=50, choices=Status.choices, default=Status.IN_WORK,
        blank=True, verbose_name='Статус'
    )

    class Meta:
        verbose_name = 'Мой заказ'
        verbose_name_plural = 'Мои заказы'
