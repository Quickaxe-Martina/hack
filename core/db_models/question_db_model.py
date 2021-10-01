from django.db import models

from accounts.models import CustomUser
from core.db_models.topic_db_model import Topic


class Question(models.Model):

    class Status(models.TextChoices):
        IN_PROGRESS = 'in_progress', 'Ожидает решения'
        CLOSED = 'closed', 'Закрыт'

    author = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, null=True,
        verbose_name='Автор вопроса', related_name='questions'
    )

    created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    topic = models.ForeignKey(
        Topic, on_delete=models.CASCADE,
        verbose_name='Тема вопроса', related_name='questions'
    )
    text = models.CharField(max_length=5000, verbose_name='Текст')

    prise = models.PositiveIntegerField(default=1, verbose_name='Награда')

    deadline = models.DateTimeField(verbose_name='Контрольный срок')
    exigent = models.BooleanField(default=False, verbose_name='Срочный вопрос')

    status = models.CharField(
        max_length=50, choices=Status.choices, default=Status.IN_PROGRESS,
        blank=True, verbose_name='Статус'
    )

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return f'{self.author} - {self.topic} - {self.created}'
