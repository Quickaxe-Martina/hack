# Generated by Django 3.2.7 on 2021-10-01 00:25

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('text', models.CharField(max_length=5000, verbose_name='Текст')),
                ('user_grade', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)], verbose_name='Оценка ответа')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='answers', to=settings.AUTH_USER_MODEL, verbose_name='Автор ответа')),
            ],
            options={
                'verbose_name': 'Ответ на вопрос',
                'verbose_name_plural': 'Ответы на вопросы',
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('score', models.BigIntegerField(default=0, verbose_name='Общий счет')),
            ],
            options={
                'verbose_name': 'Факультет',
                'verbose_name_plural': 'Факультеты',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предметы',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='core.subject', verbose_name='Предмет')),
            ],
            options={
                'verbose_name': 'Тема вопроса',
                'verbose_name_plural': 'Темы вопросов',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('text', models.CharField(max_length=5000, verbose_name='Текст')),
                ('prise', models.PositiveIntegerField(default=1, verbose_name='Награда')),
                ('deadline', models.DateTimeField(verbose_name='Контрольный срок')),
                ('exigent', models.BooleanField(default=False, verbose_name='Срочный вопрос')),
                ('status', models.CharField(blank=True, choices=[('in_progress', 'Ожидает решения'), ('closed', 'Закрыт')], default='in_progress', max_length=50, verbose_name='Статус')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='questions', to=settings.AUTH_USER_MODEL, verbose_name='Автор вопроса')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='core.topic', verbose_name='Тема вопроса')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(-1)], verbose_name='Лайк/Дизлайк')),
                ('answer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='core.answer', verbose_name='Ответ на вопрос')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to=settings.AUTH_USER_MODEL, verbose_name='Автор лайка')),
            ],
            options={
                'verbose_name': 'Лайк ответа на вопрос',
                'verbose_name_plural': 'Лайки ответов на вопросы',
            },
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='answers', to='core.question', verbose_name='Вопрос'),
        ),
    ]
