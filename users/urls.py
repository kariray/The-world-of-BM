from django.urls import path
from users.views import LoginView, logout_view, SignupView, MypageView

app_name = "users"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("signup/", SignupView.as_view(), name="signup"),
    path("<int:pk>/", MypageView.as_view(), name="mypage"),
]
