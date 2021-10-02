import os

from django.apps import AppConfig

from hack_uchi_ru_p2p import settings


class AchievementsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'achievements'

    if os.environ.get('FIRST_BUILD', False) not in ('true', 'True'):
        def ready(self):
            if settings.AI_MODEL:
                from core.tools.model_class import AIModel
                from core.db_models.question_db_model import Question

                questions = Question.objects.all()

                AIModel().prepare_model(questions)

            if settings.START_SCHEDULER:
                from core.tools.run_appscheduler import run_appscheduler

                run_appscheduler()
