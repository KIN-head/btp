from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('reqest_list.html', views.request_list, name='request_list'),
    path('reqest_new.html', views.request_new, name='request_new'),
]
