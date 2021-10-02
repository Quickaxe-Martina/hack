from django.contrib import admin

# Register your models here.
from achievements.db_models.achievement_db_model import Achievement

admin.site.register(Achievement)
