from django.urls import path
from members_app import views

urlpatterns = [
    path('', views.members_app_list, name='members_app_list'),
]