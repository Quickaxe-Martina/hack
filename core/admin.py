from django.contrib import admin

# Register your models here.
from core.db_models.answer_db_model import Answer
from core.db_models.faculty_db_model import Faculty
from core.db_models.likes_db_model import Like
from core.db_models.question_db_model import Question
from core.db_models.subject_db_model import Subject
from core.db_models.topic_db_model import Topic

admin.site.register(Answer)
admin.site.register(Faculty)
admin.site.register(Like)
admin.site.register(Question)
admin.site.register(Topic)
admin.site.register(Subject)
