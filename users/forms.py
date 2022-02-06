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


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")

    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(
        widget=forms.PasswordInput, label="Password Confirm")

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if len(first_name) <= 0:
            raise forms.ValidationError("Please input your first name.")
        else:
            return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        if len(last_name) <= 0:
            raise forms.ValidationError("Please input your last name.")
        else:
            return last_name

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            user = User.objects.get(email=email)
            raise forms.ValidationError("This email already added.")
        except User.DoesNotExist:
            if len(email) <= 0:
                raise forms.ValidationError("Please input your email.")
            else:
                return email

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password != password1:
            raise forms.ValidationError(
                "Password confirmation does not match.")
        else:
            return password

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user.username = email
        user.set_password(password)
        user.save()
