# course_search/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search-student-courses/', views.search_student_courses, name='search_student_courses'),
]
