from django.urls import path, include
from .views import RegisterTeacherAPIView, TeacherDashboardView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("teacher-dashboard",TeacherDashboardView)

urlpatterns = [
    path('teacher-register/',RegisterTeacherAPIView.as_view(), name='teacher-register'),
    path('',include(router.urls))
] 