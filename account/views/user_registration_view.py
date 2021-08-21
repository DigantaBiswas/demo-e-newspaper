from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.views import View

from account.models import UserBasedNewsConfig


class UserRegistrationView(View):
    def get(self,request):
        form = UserCreationForm(request.POST)
        return render(request, 'account/signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            UserBasedNewsConfig.create_user_config(user)

            return redirect('home')

        return render(request, 'signup.html', {'form': form})
