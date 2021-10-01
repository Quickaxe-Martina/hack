from django.db import models

from accounts.models import CustomUser
from chat.db_models.chat_db_model import Chat


class MessageChat(models.Model):
    author = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, null=True,
        verbose_name='Автор сообщения', related_name='messages'
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    chat = models.ForeignKey(
        Chat, on_delete=models.SET_NULL, null=True,
        verbose_name='Чат', related_name='messages'
    )

    text = models.CharField(max_length=5000, verbose_name='Текст')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return f'{self.author} - {self.text}'
