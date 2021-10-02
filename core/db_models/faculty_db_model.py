from django.db import models


class Faculty(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    score = models.BigIntegerField(default=0, verbose_name='Общий счет')
    image = models.ImageField(upload_to='faculty_image', verbose_name='Картинка', blank=True, null=True)

    class Meta:
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультеты'

    def __str__(self):
        return self.name
