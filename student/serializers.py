from rest_framework.serializers import ModelSerializer
from .models import Student, MyCourses
from rest_framework.exceptions import APIException

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate_first_name(self, name):
        if len(name) <= 4:
            raise APIException("First name is too short!")
        return name

    def validate_last_name(self, name):
        if len(name) <= 8:
            raise APIException("Last name is short!")
        return name

class EnrolledSerializer(ModelSerializer):
    class Meta:
        model = MyCourses
        fields = '__all__'