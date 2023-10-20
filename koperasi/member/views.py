from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout

# Create your views here.



def member(request):
    context ={
        'title':'Member'
    }
    return render(request,'member/member.html',context)

def dashboard(request):
    context ={
        'title':'Dashboard'
    }
    return render(request,'member/dashboard.html',context)

def login_member(request):
    if request.method == "POST":
        user_login = request.POST['username']
        pass_login = request.POST['password']
        user = authenticate(request, username=user_login, password=pass_login)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return redirect('member')
    context ={
        'title':'Login Member'
    }
    return render(request,'member/login.html',context)


def logout_member(request):
        logout(request)
        return redirect('member')
        


def register_member(request):
    context = {
        'title':'Register Member'
    }
    return render(request,'member/register.html',context)

def forget_password(request):
    context ={
        'title':'Reset Password'
    }
    return render(request,'member/forget-password.html',context)