from ast import Add
from django.urls import path
from .views import AllCoursesView, AddCourseView

urlpatterns = [
    path("",AllCoursesView.as_view(), name='all-courses'),
    path("add-course/",AddCourseView.as_view(), name='add-courses'),
]