
# Create your models here.
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Project(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    topic = models.CharField(max_length=200)
    languages_used = models.CharField(max_length=100)
    duration = models.IntegerField(help_text="Duration in weeks")

    def __str__(self):
        return self.topic
