from django.shortcuts import render
from django.contrib import messages
from beranda.models import Contact

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
    if request.method == "POST":
        nama = request.POST.get('nama')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if nama == "" or email == "" or  message == "":
            messages.success(request,'Form tidak boleh kosong')
            contact = Contact(nama=nama, email=email, message=message)
            contact.save()
            return render(request,'beranda/contact.html')
        
        context ={
        'title':'Contact'
        }
        return render(request,'beranda/contact.html',context)