from account.forms import AvatarForm, UserRegistrationForm
from account.models import Avatar, User

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView


class ViewMyProfile(LoginRequiredMixin, ListView):
    queryset = User.objects.all()
    template_name = 'account/user_list.html'


class MyProfile(LoginRequiredMixin, UpdateView):
    queryset = User.objects.filter(is_active=True)
    fields = ('first_name', 'last_name', 'username', 'email')
    success_url = reverse_lazy('home_page')

    def get_object(self, queryset=None):
        return self.request.user


class SignUpView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = "account/user_sign_up.html"
    success_url = reverse_lazy("home_page")


class ActivateUserView(View):
    def get(self, request, confirmation_token):
        user = get_object_or_404(User, confirmation_token=confirmation_token)
        user.is_active = True
        user.save(update_fields=("is_active",))
        return redirect("end_registration")


class AvatarCreate(LoginRequiredMixin, CreateView):
    model = Avatar
    form_class = AvatarForm
    success_url = reverse_lazy('home_page')

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(request=self.request, **self.get_form_kwargs())


class AvatarList(LoginRequiredMixin, ListView):
    queryset = Avatar.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)
