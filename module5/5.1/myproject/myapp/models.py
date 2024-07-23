from django.db import models
# Create your models here.
class Course(models.Model):
    
    course_name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.course_name
class Student(models.Model):
    
    student_name=models.CharField(max_length=100)
   
    enrolment=models.ManyToManyField(Course)
    def __str__(self):
        return self.student_name