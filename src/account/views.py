from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
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
