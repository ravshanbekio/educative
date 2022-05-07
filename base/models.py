from django.db import models
from teacher.models import Teacher
from student.models import Student

class Category(models.Model):
    category_name = models.CharField(max_length=150)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = "Course Category"

class Course(models.Model):
    owner = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name="teacher_course")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    students = models.ManyToManyField(Student, blank=True)
    course_name = models.CharField(max_length=150)
    course_description = models.TextField(max_length=300)
    course_difficulty = models.CharField(max_length=50, choices=[("Hard","Hard"),("Medium","Medium"),("Easy","Easy")])
    course_date = models.DateField(auto_now_add=True)
    course_image = models.FileField(upload_to='media', blank=True, null=True)
    course_price = models.PositiveIntegerField(default=0)
    number_of_students = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.course_name}, category - {self.cateogory.category_name}"

    class Meta:
        verbose_name_plural = "Course"

class Media(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    media_files = models.FileField(upload_to='media')

    def __str__(self):
        return self.course.course_name

    class Meta:
        verbose_name_plural = "Media"

class Statistics(models.Model):
    number_of_courses = models.IntegerField(default=0)
    number_of_teachers = models.IntegerField(default=0)
    number_of_students = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.number_of_students} students, {self.number_of_teachers} teachers, {self.number_of_courses} courses"

    class Meta:
        verbose_name_plural = "Total statistics"

class TeacherStat(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    number_of_courses = models.ManyToManyField(Course)
    
    def __str__(self):
        return self.teacher.first_name + ' ' + self.last_name

