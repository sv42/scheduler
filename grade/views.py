from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Day_grade
from django.contrib.auth.decorators import login_required

@login_required
def grades(request):
    scores = Day_grade.objects.all() 

    context = {
        'title': 'Оцінки',
        'day_grades': scores, 
    }

    return render(request, 'grade/index.html', context)

def user_profile(request):
    user = User.objects.get(id=2) 
    return render(request, 'user_profile.html', {'user': user})

def my_view(request):
    if request.method == 'POST':
        selected_date = request.POST.get('calendar')
    return render(request, 'my_template.html')

