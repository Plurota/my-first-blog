from django.urls import path
from . import views
from django.shortcuts import get_object_or_404

urlpatterns = [
	path('', views.post_list, name='post-list'),
	path('post/<int:pk>/', views.post_detail, name='post_detail'),
]