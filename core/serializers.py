from rest_framework import serializers
from .models import Reminder

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reminder
        fields=["id","title","time","created_at"]
