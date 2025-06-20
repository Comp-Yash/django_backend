from django.db import models
from django.contrib.auth.models import User

class Reminder(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    time=models.DateTimeField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.user.username})"

class TelegramProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    telegram_username=models.CharField(max_length=100)
    telegram_user_id=models.CharField(max_length=100)

    def __str__(self):
        return str(self.telegram_username)

