from django import forms
from users.models import User


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={"placeholder": "Email"}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"placeholder": "Password"}))

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        #print(f"before: {self.cleaned_data}")
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError(
                    "Password is wrong."))
        except User.DoesNotExist:
            self.add_error("email", forms.ValidationError(
                "User does not exist."))
        #print(f"after: {self.cleaned_data}")
