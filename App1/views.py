from django.shortcuts import render
from .forms import *
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    if request.method == 'GET':
        return render(request,'base.html',{'init':True})
    if request.method == 'POST':
        # get username and password
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return render(request,'base.html',{'init':True})

        else:
            return render(request,'login.html',{'err':"Wrong Credentials",'link':'{% url "login" %}'})

def user_login(request):
    custom_form = Formclass()
    if request.method == 'GET':
        return render(request,'login.html',{'form':custom_form})

@login_required()
def user_logout(request):
    if request.method == 'GET':
        logout(request)
        return HttpResponseRedirect(reverse('App1:index'))

@login_required(login_url="/login")
def user_create(request):
    custom_form = Formclass()
    if request.method == 'GET':
        return render(request,'base.html',{'form': custom_form})
    if request.method == 'POST':
        form = Formclass(request.POST)
        if form.is_valid():
            mark1 = form.cleaned_data['mark1']
            mark2 = form.cleaned_data['mark2']
            mark3 = form.cleaned_data['mark3']
            total = mark1+mark2+mark3
            avg = round(total/3,2)
            if avg >= 90:
                grade = 'A'
            elif avg >= 80:
                grade = 'B'
            elif avg >= 70:
                grade = 'C'
            elif avg >= 60:
                grade = 'D'
            else:
                grade = 'F'
            test = Student.objects.get_or_create(name=form.cleaned_data['name'],age=form.cleaned_data['age'],mark1=form.cleaned_data['mark1'],mark2=form.cleaned_data['mark2'],mark3=form.cleaned_data['mark3'],total=total,avg=avg,grade=grade)[0]
            test.save()
            return render(request,'base.html',{'msg':'User Created Successfully','link':'App1:index'})
        else:
            return render(request,'base.html',{'form':form})
@login_required(login_url="/login")
def show(request):
    data = Student.objects.order_by('avg')
    return render(request,'base.html',{'data':data})

def init(request):
    return HttpResponseRedirect(reverse('App1:index'))