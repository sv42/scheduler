from django.db import models
from bases.models import Lesson
from django.contrib.auth.models import User

class Day_grade(models.Model):  
    score = models.IntegerField("Оцінка за урок")
    leson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='day_grades')
    student_grade = models.ManyToManyField(User, related_name='day_grade', blank=True)
