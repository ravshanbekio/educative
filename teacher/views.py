from .models import Teacher
from .serializers import TeacherSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from base.models import Course, Statistics
from base.serializers import CourseSerializer

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
            stat = Statistics.objects.first()
            stat.number_of_teachers += int(Teacher.objects.all().count())
            stat.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeacherDashboardView(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated,]

    @action(detail=False, methods=["GET","POST","PATCH","DELETE"])
    def mycourse(self, request, *args, **kwargs):
        teacher = Teacher.objects.get(user=request.user)
        course = Course.objects.filter(owner=teacher)
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        return Teacher.objects.filter(user=self.request.user)