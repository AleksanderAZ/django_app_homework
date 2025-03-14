from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def members_app_list(request):
    members = User.objects.all()
    return render(request, 'members_app/members_app_list.html', {'members': members})