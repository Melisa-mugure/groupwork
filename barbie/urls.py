from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('progress/', views.progress, name='progress'),
    path('news/', views.news, name='news'),
    path('fanpage/', views.fanpage, name='fanpage'),
    path('community/', views.community, name='community')


]


