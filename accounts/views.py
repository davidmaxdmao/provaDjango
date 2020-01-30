from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView



# Create your views here.

class IndexView(TemplateView):
    template_name = 'login.html'

class RegisterView(FormView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username, password=raw_password)
        login(self.request, user)
        return redirect('index')