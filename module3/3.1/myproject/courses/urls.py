from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_student, name='register_student'),
    path('course/<int:course_id>/', views.course_details, name='course_details'),
    path('list/', views.course_list, name='course_list'),
]
