from django.urls import path
from . import views
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # post views
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    #path('login/', django.contrib.auth.views.login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    #path('logout-then-login/', django.contrib.auth.views.logout_then_login, name='logout_then_login'),
]
