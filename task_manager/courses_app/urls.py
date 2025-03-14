from django.urls import path
from courses_app import views

urlpatterns = [
    path('', views.courses_app_url, name='courses_app_url'),
    path('courses_app_guest/',views.courses_app_guest_url, name='guest_courses_app'),
]