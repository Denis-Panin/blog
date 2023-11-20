from account import views
from django.urls import path

app_name = 'account'

urlpatterns = [
    # path('my-profile/', views.MyProfile.as_view(), name='my_profile'),
    # path('view_my-profile/', views.ViewMyProfile.as_view(), name='view_my_profile'),
    # path('sign-up-old/', views.SignUpView.as_view(), name='sign_up'),
    # path('activate/<str:confirmation_token>', views.ActivateUserView.as_view(), name='activate_user_token'),
    # path('my-profile/avatar/create', views.AvatarCreate.as_view(), name='my_profile_avatar_create'),
    # path('my-profile/avatar/list', views.AvatarList.as_view(), name='my_profile_avatar_list'),

    # path('sign-in/', views.sign_in, name="sign_in"),
    path('login/', views.sign_in, name="login"),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('log-out/', views.logout_view, name="log_out"),
]
