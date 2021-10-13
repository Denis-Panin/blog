from account import views
from django.urls import path

app_name = 'account'

urlpatterns = [
    path('my-profile/', views.MyProfile.as_view(), name='my_profile'),
    path('view_my-profile/', views.ViewMyProfile.as_view(), name='view_my_profile'),
    path('sign-up/', views.SignUpView.as_view(), name='sign_up'),
    path('activate/<str:confirmation_token>', views.ActivateUserView.as_view(), name='activate_user_token'),
    path('my-profile/avatar/create', views.AvatarCreate.as_view(), name='my_profile_avatar_create'),
    path('my-profile/avatar/list', views.AvatarList.as_view(), name='my_profile_avatar_list'),
]
