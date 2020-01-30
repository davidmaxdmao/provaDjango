from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path('entrar/', auth_views.LoginView.as_view(), name='entrar'),
    path('register', views.RegisterView.as_view(), name='RegisterView'),
]
