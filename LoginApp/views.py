from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User

# This views is of LoginApp.

def my_login(request):
    
    if request.method=='POST':
        
        username=request.POST['us']
        password=request.POST['pw']

        user=authenticate(request=request,username=username,password=password)
        context={
            "user":username,
            "url":"login"
        }
        if user is not None:
            login(request,user)
            return render(request,'login/loggedin.html',context=context)
        else:
            return HttpResponse('<h1><center>Invalid password or username</center></h1>')

    elif request.method=='GET':

        return render(request,'login/login.html')
def my_logout(request):
    logout(request)
    return render(request,'index.html')
def my_register(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pw=request.POST.get('pasw')
        cpw=request.POST.get('conpw')
        if pw==cpw:
            user=User.objects.create_user(uname,email=email,password=pw)
            user.save()
            return redirect("/login")
        else:
            return HttpResponse("<h1> Password was not matched </h1>")
        
    elif request.method=='GET':
        return render(request,'login/register.html')

def foruser(request):
    if request.user.is_authenticated:
        return render(request,'login/foruser.html')
    else:
        return redirect("/login")


    