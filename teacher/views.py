from .models import Teacher
from .serializers import TeacherSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

class RegisterTeacherAPIView(APIView):
    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            a = Teacher.objects.last()
            new_user = User.objects.create(
                username=a.username
            )
            new_user.save()
            a.user = new_user
            a.save()    
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeacherDashboardView(APIView):
    def get(self, request):
        teacher = Teacher.objects.get(user=request.user)
        if teacher.is_active == True:
            serializer = TeacherSerializer(teacher)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message':"Teacher is not activated"})