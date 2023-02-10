from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View

from users.forms import UserCreationFormByMe


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationFormByMe()  # Дефолт форма регистрации
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationFormByMe(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        context = {   # При не прохожденнии валидации вернуть -->
            'form': form
        }
        return render(request, self.template_name, context)
