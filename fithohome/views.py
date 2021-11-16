from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import blogs
from .form import userform


def homepage(request):
    return render( request,"homepage.html")

def signup(request):
    if(request.method=="POST"):
        username=request.POST['username']
        password=request.POST['password']
        password2=request.POST['password2']
        email=request.POST['email']
        if(password==password2):
            if User.objects.filter(username=username).exists():
                messages.info(request,"user already exists")
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"user already exists")
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,password=password)  
                user.save();
                return redirect("login")
        else:
            messages.info(request,"password is not same")
            return redirect("signup")
    else:
        return render(request,"signup.html")

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)
        if user is not None:
             auth.login(request,user)
             return redirect("/")
        else:
            messages.info(request,"you are not our member or something may be wrong")
            return redirect("login")
    else:
        return render(request,"login.html")
   
def blog(request):
    blog=blogs.objects.all()
    return render(request,"blog.html",{'blogs':blog})

def aboutus(request):
    return render(request,"aboutus.html")

def renting(request):
    return render(request,"renting.html")

def inputform(request):
    form=userform()
    if request.method=='POST':
        form=userform(request.POST)
        if form.is_valid():
            data=form.save()
            data1=form.cleaned_data['name']
            data2=form.cleaned_data['phone']
            data3=form.cleaned_data['email']
            data4=form.cleaned_data['height']
            data5=form.cleaned_data['weight']
            data6=form.cleaned_data['fat']
            data7=form.cleaned_data['build']
            print(data1)
            print(data2)
            print(data3)
            print(data4)
            print(data5)
            print(data6)
            print(data7)
        else:
            pass
    else:
        pass

    return render(request,"userform.html",{'form':form})


def logout(request):
    auth.logout(request)
    return redirect("/")