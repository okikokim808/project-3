from django.shortcuts import render, redirect
from afterschool.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, QueryDict
from .models import Student, Parent, DailyInfo, User
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    return render(request, 'afterschool/index.html')

def about(request):
    return render(request, 'afterschool/about.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('index')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print(f'They used username: {username} and password: {password}')
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'afterschool/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

@login_required
def account(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    parent = Parent.objects.get(user=user)
    return render(request, 'afterschool/account.html', {'parent': parent})
    
@login_required
def daycare_info(request):
    user_id = request.user
