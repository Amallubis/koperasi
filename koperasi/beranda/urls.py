from django.urls import path
from beranda import views

urlpatterns = [
    path('',views.beranda,name='beranda'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact')
    
]
