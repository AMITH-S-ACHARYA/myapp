# myapp/urls.py
from django.urls import path
from .views import course_search_ajax

urlpatterns = [
    path('course_search_ajax/', course_search_ajax, name='course_search_ajax'),
]

