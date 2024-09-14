# Методи при переході юзера
from django.shortcuts import render
from django.contrib.auth.models import User
from bases .models import SchoolClass
from grade .models import Day_grade
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.core.cache import cache
from django.http import HttpResponse
from django.contrib.auth import logout

@login_required
def logout_and_clear_cache(request):
    cache.clear()  
    return redirect('your-redirect-url') 

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Отримуємо ім'я користувача та пароль із форми
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})

@login_required
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
