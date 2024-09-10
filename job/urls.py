from django.urls import path
from .views import job_list, job_detail, post_job

app_name= 'job'

urlpatterns = [
    path('', job_list, name='job_list'),
    path('post_job/', post_job, name='post_job'),
    path('<str:slug>', job_detail, name='job_detail'),
]