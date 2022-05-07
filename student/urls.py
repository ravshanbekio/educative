from django.urls import path
from .views import StudentRegisterView, StudentDashboardView

urlpatterns = [
    path('student-register/',StudentRegisterView.as_view(), name='student-register'),
    path('student-dashboard/',StudentDashboardView.as_view(), name='student-dashboard')
]