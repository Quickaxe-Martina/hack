import os

from django.apps import AppConfig


class AchievementsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'achievements'

    if os.environ.get('FIRST_BUILD', False) not in ('true', 'True'):
        def ready(self):
            from core.tools.model_class import AIModel
            from core.db_models.question_db_model import Question

            questions = Question.objects.all()

            AIModel().prepare_model(questions)
