from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from accounts.models import CustomUser
from core.db_models.answer_db_model import Answer


class Like(models.Model):
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, null=True,
        verbose_name='Автор лайка', related_name='likes'
    )

    answer = models.ForeignKey(
        Answer, on_delete=models.CASCADE, null=True,
        verbose_name='Ответ на вопрос', related_name='likes'
    )

    type = models.IntegerField(
        verbose_name='Лайк/Дизлайк',
        validators=[
            MaxValueValidator(1),
            MinValueValidator(-1)
        ]
    )

    class Meta:
        verbose_name = 'Лайк ответа на вопрос'
        verbose_name_plural = 'Лайки ответов на вопросы'

    def __str__(self):
        return f'{self.author} - {self.answer} - {self.type}'
