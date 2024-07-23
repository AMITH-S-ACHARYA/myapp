
from django.db import models

class Course(models.Model):
    course_code=models.CharField(max_length=100)
    course_name=models.CharField(max_length=100)
    course_credits=models.IntegerField(blank=True,null=True)

    