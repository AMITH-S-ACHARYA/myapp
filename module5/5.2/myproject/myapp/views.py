# course_search/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import Student

def search_student_courses(request):
    if request.method == 'GET':
        student_name = request.GET.get('student_name', None)
        if student_name:
            try:
                student = Student.objects.get(name=student_name)
                courses = student.courses.all()
                course_names = [course.name for course in courses]
                return JsonResponse({'courses': course_names})
            except Student.DoesNotExist:
                return JsonResponse({'courses': []})
        else:
            return JsonResponse({'error': 'Please provide a student name'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

def home(request):
    return render(request, 'index.html')

