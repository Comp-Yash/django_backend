from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_reminder_email(user_email,reminder_title):
    subject="Your Reminder was Created"
    message=f"Reminder '{reminder_title}' has been successfully created."
    from_email=settings.DEFAULT_FROM_EMAIL
    send_mail(subject, message, from_email,[user_email])
