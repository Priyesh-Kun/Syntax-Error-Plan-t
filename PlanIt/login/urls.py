from django.contrib import admin
from django.urls import path
from login import views

urlpatterns = [
    
    path('',views.index,name='index'),
    path('signup',views.sign_up,name='signup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout')
]