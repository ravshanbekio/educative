from rest_framework.serializers import ModelSerializer
from .models import Course, Media

class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class MediaSerializer(ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'