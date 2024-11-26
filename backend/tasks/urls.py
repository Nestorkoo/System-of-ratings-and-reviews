
from django.contrib import admin
from users.views import *
from django.urls import path
from tasks.views import ReviewCreateView, ReviewViewList, ReviewDeleteView,StatisticReviewView

urlpatterns = [
    path('create/', ReviewCreateView.as_view(), name='create_review'),
    path('reviews/', ReviewViewList.as_view(), name='user_reviews'),
    path('delete/<int:pk>/', ReviewDeleteView.as_view(), name='delete_review'),
    path('statistic/<str:company>/', StatisticReviewView.as_view(), name='statistic_by_company')
]
