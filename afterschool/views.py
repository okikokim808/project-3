from django.shortcuts import render, redirect
from afterschool.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, QueryDict
from .models import Student, Parent, DailyInfo, User
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        userName = User.objects.get(username=username)
        parent = Parent.objects.get(user=userName)
        if parent.is_staff:
            if user.is_active:
                login(request,user)
                return redirect('index')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print(f'They used username: {username} and password: {password}')
            return HttpResponse("Invalid login details given")
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

def staff_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        userName = User.objects.get(username=username)
        parent = Parent.objects.get(user=userName)
        if parent.is_staff:
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
        return render(request, 'afterschool/staff_login.html', {})


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
def staff(request):
    students = Student.objects.filter()
    return render(request, 'afterschool/staff.html', {'students': students})

@login_required
def student_signin(request):
    print('LOOK AT ME RIGHT HERE',request.body)
    is_signedin = True
    print(is_signedin)
    name = request.POST['name']
    print(name)
    student = Student.objects.get(name=name)
    student.is_signedin = is_signedin
    student.save()
    myDate = datetime.now()
    formatedDate = myDate.strftime("%Y-%m-%d %H:%M:%S")
    daily_info = DailyInfo.objects.create(student=student, checkin=formatedDate, checkout=formatedDate)
    daily_info.save()
    # taco = DailyInfo.objects.create(student = student,date = ,checkin =,checkout =)
    return JsonResponse({"success": True})

def student_signout(request):
    print('LOOK AT ME RIGHT HERE',request.body)
    is_signedin = False
    print(is_signedin)
    name = request.POST['name']
    print(name)
    student = Student.objects.get(name=name)
    student.is_signedin = is_signedin
    student.save()
    # taco = DailyInfo.objects.create(student = student,date = ,checkin =,checkout =)
    return JsonResponse({"success": True})

@login_required
def daycare_info(request):
    # name = request.POST['name']
    # print(name)
    # student = Student.objects.get(name=name)
    # dailyInfos = DailyInfo.objects.filter(student=student){'dailyInfos':dailyInfos}
    return render(request, 'afterschool/daycare.html' )
