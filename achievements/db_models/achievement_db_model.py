from django.db import models


class Achievement(models.Model):
    name = models.CharField(max_length=500, verbose_name='Имя')
    text = models.CharField(max_length=1000, verbose_name='Описание')

    image = models.ImageField(
        upload_to='achievement_image',
        blank=True, null=True, verbose_name='Картинка'
    )
    y_coin = models.PositiveIntegerField(default=0, verbose_name='Награда в валюте')
    f_coin = models.PositiveIntegerField(default=0, verbose_name='Награда факультету')

    map_type = models.IntegerField(unique=True)

    class Meta:
        verbose_name = 'Достижение'
        verbose_name_plural = 'Достижения'

    def __str__(self):
        return f'{self.name}'
