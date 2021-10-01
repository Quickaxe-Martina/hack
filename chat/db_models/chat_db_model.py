from django.db import models

from accounts.models import CustomUser
from core.db_models.question_db_model import Question


class Chat(models.Model):
    class TypeChat(models.TextChoices):
        GROUP = 'group', 'Групповой чат'
        PERSONAL = 'personal', 'Персональный чат'

    users = models.ManyToManyField(CustomUser, blank=True)

    type_chat = models.CharField(
        max_length=50, choices=TypeChat.choices, verbose_name='Тип чата'
    )

    question = models.ForeignKey(
        Question, on_delete=models.SET_NULL, null=True,
        verbose_name='Вопрос', related_name='chats'
    )

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'

    def __str__(self):
        return f'{self.question} - {self.type_chat}'
