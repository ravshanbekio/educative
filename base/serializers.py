from rest_framework.serializers import ModelSerializer
from .models import Course, Media, Statistics

class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class MediaSerializer(ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'

class StatSerializer(ModelSerializer):
    class Meta:
        model = Statistics
        fields = '__all__'