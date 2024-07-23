import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'thirteen.settings')
django.setup()

from myapp.models import Course, Student


course1 = Course(course_code="IS101", course_name="FULLSTACK Development", course_credits=3)
course1.save()

course2 = Course(course_code="CS101", course_name="Calculus", course_credits=4)
course2.save()


student1 = Student(student_usn="USN1", student_name="Diya", student_sem=6)
student1.save()

student2 = Student(student_usn="USN2", student_name="Priti", student_sem=5)
student2.save()

student3 = Student(student_usn="USN3", student_name="Ayra" , student_sem=4)
student3.save()

student1.enrolment.add(course1, course2)
student2.enrolment.add(course1)
student3.enrolment.add(course1 , course2)


student1.save()
student2.save()
student3.save()

