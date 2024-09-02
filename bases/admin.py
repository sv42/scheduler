from django.contrib import admin
from .models import Subject
from .models import Lesson
from .models import Teacher
from .models import Homework
from .models import SchoolClass


admin.site.register(Subject)
admin.site.register(Lesson)
admin.site.register(Teacher)
admin.site.register(Homework)
admin.site.register(SchoolClass)
