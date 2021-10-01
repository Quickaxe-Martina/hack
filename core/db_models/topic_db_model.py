from django.db import models

from core.db_models.subject_db_model import Subject


class Topic(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE,
        verbose_name='Предмет', related_name='topics'
    )

    class Meta:
        verbose_name = 'Тема вопроса'
        verbose_name_plural = 'Темы вопросов'

    def __str__(self):
        return self.name
