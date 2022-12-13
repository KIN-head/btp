from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.request_list, name='request_list'),
]
