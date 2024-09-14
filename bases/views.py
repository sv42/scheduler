# views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Subject, Lesson, Teacher, Homework, SchoolClass
from django.contrib.auth.models import Group,User
from django.contrib.auth.decorators import login_required

@login_required
def bases_home(request):
    user_groups = request.user.groups.values_list('id', flat=True)

    lessons = Lesson.objects.filter(groups__in=user_groups).distinct()
    teachers = Teacher.objects.all()
    subjects = Subject.objects.all()
    homework = Homework.objects.all()

    context = {
        'lessons': lessons,
        'teachers': teachers,
        'subjects': subjects,
        'homework': homework
    }

    return render(request, 'bases/index.html', context)



def my_view(request):
    if request.method == 'POST':
        selected_date = request.POST.get('calendar')
    return render(request, 'my_template.html')

def user_profile(request):
    user = User.objects.get(id=2) 
    return render(request, 'user_profile.html', {'user': user})


def user_class_view(request):
    user_class = SchoolClass.objects.filter(students=request.user).first()

    return render(request, 'your_template.html', {'user_class': user_class})

