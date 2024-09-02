# Методи при переході юзера
from django.shortcuts import render
from django.contrib.auth.models import User
from bases .models import SchoolClass

def index(request):
    data = {
        'title': 'Головна'
    }
    return render(request, 'main/index.html', data)

def user_profile(request):
    user = User.objects.get(id=2) 
    return render(request, 'user_profile.html', {'user': user})

def user_class_view(request):
    user_class = SchoolClass.objects.filter(classes=request.user).first()
    
    return render(request, 'your_template.html', {'user_class': user_class})
