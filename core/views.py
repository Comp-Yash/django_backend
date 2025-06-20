from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from .models import Reminder
from .serializers import ReminderSerializer
from .tasks import send_reminder_email

class PublicReminderView(APIView):
    permission_classes=[AllowAny]

    def get(self,request):
        data={"message": "Welcome to NotifyMe Public API!"}
        return Response(data)

class ReminderListCreateView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request):
        reminders=Reminder.objects.filter(user=request.user)
        serializer=ReminderSerializer(reminders,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=ReminderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            send_reminder_email.delay(request.user.email,serializer.validated_data['title'])
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
