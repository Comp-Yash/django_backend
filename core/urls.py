from django.urls import path
from .views import PublicReminderView, ReminderListCreateView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("public/", PublicReminderView.as_view(),name="public"),
    path("reminders/", ReminderListCreateView.as_view(),name="reminders"),
    path("login/", obtain_auth_token, name="login"),  # Token-based login
]
