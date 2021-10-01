from django.db import models


class Faculty(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    score = models.BigIntegerField(default=0, verbose_name='Общий счет')

    class Meta:
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультеты'

    def __str__(self):
        return self.name
