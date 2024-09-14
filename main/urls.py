from django.urls import path
from . import views
from .views import logout_and_clear_cache


urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login_view, name='login'),
    path('login/', logout_and_clear_cache, name='logout_and_clear_cache'),
]


