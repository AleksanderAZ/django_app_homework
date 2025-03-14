from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required(login_url='/courses_app/courses_app_guest/')
def courses_app_url(request):
    return render(request, 'courses_app/courses_app_url.html')

def courses_app_guest_url(request):
    return render(request, 'courses_app/courses_app_guest_url.html')
    
