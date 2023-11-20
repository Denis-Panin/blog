from django import forms

from django.contrib.auth.forms import UsernameField

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class logForm(forms.Form):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True}))
    password = forms.CharField(
        label="Password MY FORM",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )


class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# =================================================================

# class UserRegistrationForm(forms.ModelForm):
#     password_1 = forms.CharField(widget=forms.PasswordInput)
#     password_2 = forms.CharField(widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ("username", "email", "first_name", "last_name")
#
#     def clean(self):
#         clean_data: dict = super().clean()
#         if clean_data["password_1"] != clean_data["password_2"]:
#             self.add_error("password_1", "Password mismatch.")
#             # raise forms.ValidationError("Password mismatch")
#
#         return clean_data
#
#     def clean_email(self):
#         email = self.cleaned_data["email"]
#         if User.objects.filter(email=email).exists():
#             self.add_error("email", "Email already exists.")
#         return email
#
#     def save(self, commit=True):
#         instance: User = super().save(commit=False)
#         instance.is_active = False
#
#         instance.save()
#
#         # send_email_with_activation_link.delay(instance.id)
#         send_email_with_activation_link.apply_async(args=[instance.id], countdown=10)
#
#         return instance
#
#
# class AvatarForm(forms.ModelForm):
#     class Meta:
#         model = Avatar
#         fields = ('file_path',)
#
#     def __init__(self, request, *args, **kwargs):
#         self.request = request
#         super().__init__(*args, **kwargs)
#
#     def save(self, commit=False):
#         instance = super().save(commit=False)
#         instance.user = self.request.user
#         instance.save()
#         return instance
