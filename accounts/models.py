from django.contrib.auth.models import AbstractUser
from django.db import models

from achievements.db_models.achievement_db_model import Achievement
from core.db_models.faculty_db_model import Faculty


class CustomUser(AbstractUser):

    class Role(models.TextChoices):
        TEACHER = 'teacher', 'Учитель'
        STUDENT = 'student', 'Ученик'

    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=150, blank=True, default='', verbose_name='Отчество')

    email = models.EmailField(verbose_name='Почта', null=True, blank=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    level = models.FloatField(default=0.0, verbose_name='Уровень')
    exp_count = models.BigIntegerField(default=0, verbose_name='Количество опыта')

    y_coin = models.FloatField(default=0.0, verbose_name='Валюта')

    faculty = models.ForeignKey(
        Faculty, on_delete=models.SET_NULL, verbose_name='Факультет',
        null=True, blank=True, related_name='custom_users'
    )
    faculty_count = models.PositiveIntegerField(default=0, verbose_name='Очки факультета')

    avatar = models.ImageField(upload_to='user_avatar', verbose_name='Аватар', blank=True)

    birthday = models.DateField(blank=True, null=True, verbose_name='День рождения')

    instagram = models.URLField(blank=True, null=True, verbose_name='Инстаграм')

    role = models.CharField(
        max_length=50, choices=Role.choices, default=Role.STUDENT,
        blank=True, verbose_name='Роль'
    )

    referral = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True
    )

    achievement = models.ManyToManyField(Achievement, blank=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

    def add_coins(self, coins):
        self.y_coin += coins
        if self.referral:
            self.referral.y_coin += coins * 0.1
            self.referral.save()
        self.save()

    def add_faculty_count(self, faculty_count):
        self.faculty_count += faculty_count
        if self.faculty:
            self.faculty.score += faculty_count
            self.faculty.save()
        self.save()

    def add_exp(self, exp_count):
        self.exp_count += exp_count
        self.level = exp_count / 100.0
        self.save()
