from django.urls import path
from users.views import LoginView, logout_view, SignupView, MypageView, EditProfileView, ChangePasswordView

app_name = "users"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("signup/", SignupView.as_view(), name="signup"),
    path("<int:pk>/", MypageView.as_view(), name="mypage"),
    path("update-profile/", EditProfileView.as_view(), name="update_profile"),
    path("change-password/", ChangePasswordView.as_view(), name="change_password"),
]
