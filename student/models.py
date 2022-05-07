from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_data')
    image = models.FileField(upload_to='media',blank=True, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "Student"

class MyCourses(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(settings.ACC, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.student.first_name + ' ' + self.student.last_name