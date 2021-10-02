from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

from hack_uchi_ru_p2p import settings

DEFAULT_JOB_PARAMS = {
    'max_instances': 1,
    'replace_existing': True,
}


def update_questions():
    from core.tools.model_class import AIModel
    from core.db_models.question_db_model import Question

    AIModel().clear()
    questions = Question.objects.all()

    AIModel().prepare_model(questions)
    print('update_questions')
    print(AIModel().questions)


JOBS_TO_RUN = [
    # {
    #     'func': lambda: print("***GGG***"),
    #     # 'trigger': CronTrigger(hour='04', minute='05'),
    #     'trigger': CronTrigger(minute='*/1'),  # every minute for debug
    # },
    {
        'func': update_questions,
        # 'trigger': CronTrigger(minute='*/15'),
        'trigger': CronTrigger(minute='*/30'),  # every minute for debug
    },
]


def get_job_params(job: dict):
    job_params = dict(DEFAULT_JOB_PARAMS, id=job['func'].__name__)
    job_params.update(job)
    return job_params


def run_appscheduler():
    scheduler = BackgroundScheduler(timezone=settings.TIME_ZONE)
    for job in JOBS_TO_RUN:
        scheduler.add_job(**get_job_params(job))
    scheduler.start()
