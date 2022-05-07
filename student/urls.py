from django.urls import path, include
from .views import StudentRegisterView, StudentDashboardView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("student-dashboard",StudentDashboardView)

urlpatterns = [
    path('student-register/',StudentRegisterView.as_view(), name='student-register'),
    path('',include(router.urls)),
]