from django.shortcuts import render
from .models import Day_grade


def index(request):
    data = {
        'title': 'Оцінки'
    }
    return render(request, 'grade/index.html', data)

def grades(request):
    Score = Day_grade.objects.all()

    context = {
        'day_grade': Score,
        
    }

    return render(request, 'grade/index.html', context)
