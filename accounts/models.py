from django.contrib.auth.models import AbstractUser
from django.db import models

from core.db_models.faculty_db_model import Faculty


class CustomUser(AbstractUser):

    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=150, blank=True, default='', verbose_name='Отчество')

    email = models.EmailField(verbose_name='Почта', null=True, blank=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    level = models.FloatField(default=0.0, verbose_name='Уровень')
    exp_count = models.BigIntegerField(default=0, verbose_name='Количество опыта')

    y_coin = models.PositiveIntegerField(default=0, verbose_name='Валюта')

    faculty = models.ForeignKey(
        Faculty, on_delete=models.SET_NULL, verbose_name='Факультет',
        null=True, blank=True, related_name='custom_users'
    )
    faculty_count = models.PositiveIntegerField(default=0, verbose_name='Очки факультета')

    avatar = models.ImageField(upload_to='user_avatar', verbose_name='Аватар', blank=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
