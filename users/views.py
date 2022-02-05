from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.views import View
from users.forms import LoginForm

# Create your views here.


def logout_view(request):
    """Logout"""
    logout(request)
    return redirect(reverse("core:home"))


class LoginView(View):
    """Login"""

    def get(self, request):
        form = LoginForm()
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        # print(form.errors)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            print("start")
            print(f"{email}, {password}")
            print(user)
            if user is not None:
                login(request, user)
                print("user")
                return redirect(reverse("core:home"))

        return render(request, "users/login.html", {"form": form})
