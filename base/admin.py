from django.contrib import admin
from .models import Course, Category, Media, Statistics, TeacherStat

admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Media)
admin.site.register(Statistics)
admin.site.register(TeacherStat)