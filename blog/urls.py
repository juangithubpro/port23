from django.urls import path
from .views import rende_post, post_detail

app_name = 'blog'

urlpatterns = [
    path('', rende_post, name='posts'),
    path('<int:post_id>', post_detail, name='post_detail'),
]




