from django.contrib import admin

# Register your models here.
from chat.db_models.chat_db_model import Chat
from chat.db_models.message_db_model import MessageChat

admin.site.register(Chat)
admin.site.register(MessageChat)
