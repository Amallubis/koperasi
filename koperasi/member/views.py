from django.shortcuts import render

# Create your views here.

def member(request):
    context ={
        'title':'Member'
    }
    return render(request,'member/member.html',context)