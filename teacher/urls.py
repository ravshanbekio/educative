from django.urls import path
from .views import RegisterTeacherAPIView, TeacherDashboardView

urlpatterns = [
    path('teacher-register/',RegisterTeacherAPIView.as_view(), name='teacher-register'),
    path('teacher-dashboard/',TeacherDashboardView.as_view(), name='teacher-dashboard'),
] 