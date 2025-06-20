from django.contrib import admin
from .models import Reminder, TelegramProfile

admin.site.register(Reminder)
admin.site.register(TelegramProfile)
