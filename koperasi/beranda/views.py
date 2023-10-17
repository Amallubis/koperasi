from django.shortcuts import render

# Create your views here.

def beranda(request):
    context ={
        'title':'Koperasi UKMandiri'
    }
    return render(request,'beranda/beranda.html',context)

def about(request):
    context ={
        'title':'About Me'
    }
    return render(request,'beranda/about.html',context)

def contact(request):
    context ={
        'title':'Contact'
    }
    return render(request,'beranda/contact.html',context)