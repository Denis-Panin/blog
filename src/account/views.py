from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import redirect, render

from .forms import LogInForm, SignUpForm


def sign_in(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.POST.get(
                    'next',
                    request.GET.get('next', None)
                )
                if next_url:
                    return redirect(next_url)
                else:
                    return redirect('blog:home_page')
    else:
        form = LogInForm()
    return render(
        request,
        'account/login.html',
        {'form': form}
    )


def sign_up(request):
    account_created = False
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            account_created = True
            messages.success(request, 'Account created')
            form = SignUpForm()
    else:
        form = SignUpForm()
    return render(request, 'account/sign-up.html',
                  {'form': form, 'account_created': account_created})


def logout_view(request):
    logout(request)
    return redirect('blog:home_page')
# =================================================================================================

# class ViewMyProfile(LoginRequiredMixin, ListView):
#     queryset = User.objects.all()
#     template_name = 'account/user_list.html'
#
#
# class MyProfile(LoginRequiredMixin, UpdateView):
#     queryset = User.objects.filter(is_active=True)
#     fields = ('first_name', 'last_name', 'username', 'email')
#     success_url = reverse_lazy('home_page')
#
#     def get_object(self, queryset=None):
#         return self.request.user
#
#
# class SignUpView(CreateView):
#     model = User
#     form_class = UserRegistrationForm
#     template_name = "account/user_sign_up.html"
#     success_url = reverse_lazy("home_page")
#
#
# class ActivateUserView(View):
#     def get(self, request, confirmation_token):
#         user = get_object_or_404(User, confirmation_token=confirmation_token)
#         user.is_active = True
#         user.save(update_fields=("is_active",))
#         return redirect("end_registration")
#
#
# class AvatarCreate(LoginRequiredMixin, CreateView):
#     model = Avatar
#     form_class = AvatarForm
#     success_url = reverse_lazy('home_page')
#
#     def get_form(self, form_class=None):
#         if form_class is None:
#             form_class = self.get_form_class()
#         return form_class(request=self.request, **self.get_form_kwargs())
#
#
# class AvatarList(LoginRequiredMixin, ListView):
#     queryset = Avatar.objects.all()
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         return queryset.filter(user=self.request.user)
