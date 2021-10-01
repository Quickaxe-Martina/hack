from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from accounts.models import CustomUser
from core.db_models.question_db_model import Question


class Answer(models.Model):
    author = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, null=True,
        verbose_name='Автор ответа', related_name='answers'
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    text = models.CharField(max_length=5000, verbose_name='Текст')

    question = models.ForeignKey(
        Question, on_delete=models.SET_NULL, null=True,
        verbose_name='Вопрос', related_name='answers'
    )

    # TODO: лучший ответ и прочее
    user_grade = models.PositiveIntegerField(
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ],
        verbose_name='Оценка ответа'
    )

    class Meta:
        verbose_name = 'Ответ на вопрос'
        verbose_name_plural = 'Ответы на вопросы'

    def __str__(self):
        return f'{self.author} - {self.question} - {self.created}'
