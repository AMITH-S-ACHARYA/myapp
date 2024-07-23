
from django.http import JsonResponse
from django.shortcuts import render
from .models import Course, Student

def course_search_ajax(request):
    if request.method == "POST":
        cid = request.POST.get("cname")
        students = Student.objects.filter(enrolment__id=cid).distinct()
        student_list = [
            {
                "name": student.student_name,
                "usn": student.student_usn,
                "sem": student.student_sem,
            }
            for student in students
        ]
        return JsonResponse({"students": student_list})

    else:
        courses = Course.objects.all()
        return render(request, "course_search_aj.html", {"courses": courses})

