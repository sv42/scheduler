from django.db import models
from django.contrib.auth.models import User, Group

class Subject(models.Model):
    title = models.CharField('Назва', max_length=50)
    science = models.CharField('Наука', max_length=50)
    
    def __str__(self):
        return self.title

class Teacher(models.Model):
    name = models.CharField('ПІБ', max_length=100)
    
    def __str__(self):
        return self.name

class Lesson(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='lessons')
    start = models.DateTimeField('Початок')
    finish = models.DateTimeField('Кінець')
    duration = models.TimeField('Тривалість')  
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='lessons')
    groups = models.ManyToManyField(Group, related_name='lessons', blank=True)
    
    def __str__(self):
        return f'{self.subject.title}'

class Homework(models.Model):
    task = models.CharField('Домашнє завдання', max_length=100)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='homeworks')
    
    def __str__(self):
        return self.task

class SchoolClass(models.Model):  
    grade = models.IntegerField("Клас")
    students = models.ManyToManyField(Group, related_name='school_classes')
    
    
    def __str__(self):
        return f'Клас {self.grade}'
