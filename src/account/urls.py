from account import views
from django.urls import path

app_name = 'account'

urlpatterns = [
    path('login/', views.sign_in, name='login'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('log-out/', views.logout_view, name='log_out'),
]
