from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.views.generic import FormView, DetailView, UpdateView
from django.contrib.auth.views import PasswordChangeView
from users.forms import LoginForm, SignUpForm
from users.models import User

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


class SignupView(FormView):
    """Sign up"""
    template_name = "users/signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


class MypageView(DetailView):
    """Show user's my page."""
    model = User
    template_name = "users/my_page.html"
    context_object_name = "user_obj"


class EditProfileView(UpdateView):
    """Edit user's profile"""
    model = User
    template_name = "users/update_profile.html"
    context_object_name = "user_obj"
    fields = (
        "first_name",
        "last_name",
        "bio",
        "avatar",
        "preference",
        "language",
        "fav_book_genre",
        "fav_movie_genre",
    )

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy("users:mypage", kwargs={"pk": self.object.pk})


class ChangePasswordView(PasswordChangeView):
    """Change user's password"""
    template_name = "users/change_password.html"
    success_url = reverse_lazy("core:home")
