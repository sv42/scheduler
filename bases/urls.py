from django.urls import path
from . import views

urlpatterns = [
    path('', views.bases_home, name='bases_home')
]
