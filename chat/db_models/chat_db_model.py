from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from accounts.models import CustomUser
from core.db_models.question_db_model import Question


class Chat(models.Model):
    class TypeChat(models.TextChoices):
        GROUP = 'group', 'Групповой чат'
        PERSONAL = 'personal', 'Персональный чат'

    users = models.ManyToManyField(
        CustomUser, blank=True, related_name='chat_users',
        through='ThroughUserChat'
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

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


class ThroughUserChat(models.Model):
    chat = models.ForeignKey(Chat, related_name='through_chat', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, related_name='through_user', on_delete=models.CASCADE)
    is_organizer = models.BooleanField(default=False, verbose_name='Создатель чата')
    user_grade = models.PositiveIntegerField(
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ],
        verbose_name='Оценка помощи'
    )

    class Meta:
        unique_together = ['chat', 'user']
