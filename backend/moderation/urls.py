
from django.contrib import admin
from users.views import *
from django.urls import path
from moderation.views import *

urlpatterns = [
    path('reports/', ReportListView.as_view(), name='get_all_reports'),
    path('create_report/<int:review_id>/', CreateReportView.as_view(), name='create_reports'),
    path('delete_review/', DeleteReviewView.as_view(), name='delete_review'),

]