from rest_framework import status
from rest_framework.response import Response
from .models import Course
from .serializers import CourseSerializer
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from teacher.models import Teacher
from rest_framework.views import APIView

class AllCoursesView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated,]

class AddCourseView(APIView):
    def post(self, request):
        teacher = Teacher.objects.get(user=request.user)
        if teacher.is_active == True:
            serializer = CourseSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message':"Teacher is not activated!"})