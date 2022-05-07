from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from base.models import Course
from base.serializers import CourseSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

class StudentRegisterView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated,]

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