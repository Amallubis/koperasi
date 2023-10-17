from django.shortcuts import render

# Create your views here.

def member(request):
    context ={
        'title':'Member'
    }
    return render(request,'member/member.html',context)

def login_member(request):
    context ={
        'title':'Login Member'
    }
    return render(request,'member/login.html',context)


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