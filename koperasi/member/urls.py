from django.urls import path
from member import views

urlpatterns = [
    path('member/',views.member, name='member')
]
