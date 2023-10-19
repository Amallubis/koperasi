from django.urls import path
from member import views

urlpatterns = [
    path('member/',views.member, name='member'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('login/',views.login_member,name='login'),
    path('register/',views.register_member,name='register'),
    path('forger-password/',views.forget_password,name='forget-password'),
]
