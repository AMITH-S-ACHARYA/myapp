
# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Course, Student

def register_student(request):
    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        course_id = request.POST.get('course')
        course = get_object_or_404(Course, pk=course_id)
        student = Student.objects.create(name=student_name)
        student.courses.add(course)
    courses = Course.objects.all()
    return render(request, 'register_student.html', {'courses': courses})

def course_details(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    students = course.students.all()
    return render(request, 'course_details.html', {'course': course, 'students': students})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})
