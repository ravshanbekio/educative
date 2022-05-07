from .models import Student
from .serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from base.models import Course, Statistics
from base.serializers import CourseSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework import status

from django.contrib.auth.models import User

class StudentRegisterView(APIView):
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            a = Student.objects.last()
            new_user = User.objects.create(
                username=a.username
            )
            new_user.save()
            a.user = new_user
            a.save()
            stat = Statistics.objects.first()
            stat.number_of_students += int(Student.objects.all().count())
            stat.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDashboardView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated,]

    @action(detail=False, methods=["GET"])
    def mycourse(self, request, *args, **kwargs):
        student = Student.objects.get(user=request.user)
        course = Course.objects.filter(students=student)
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        return Student.objects.filter(user=self.request.user)