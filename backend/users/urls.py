
from django.contrib import admin
from users.views import *
from django.urls import path

urlpatterns = [
    path('register/',UserRegistrationView.as_view(), name='user_registration'),
    path('login/', UserLoginView.as_view(), name='user_auth'),
    path('profile/<str:username>/', UserProfileView.as_view(), name='user_profile')
]
