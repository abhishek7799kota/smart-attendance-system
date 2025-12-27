from django.urls import path
from . import views

urlpatterns = [
    # Teacher login
    path('teacher-login/', views.teacher_login, name='teacher_login'),
    path('logout/', views.user_logout, name='logout'),

    # Teacher pages
    path('teacher/', views.dashboard, name='dashboard'),
    path('mark/', views.mark_attendance, name='mark_attendance'),
    path('report/', views.attendance_report, name='attendance_report'),

    # Student (NO LOGIN)
    path('student/', views.student_attendance, name='student_attendance'),
]
