from django.urls import path
from . import views

urlpatterns = [
    # path del core
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('sample/', views.sample, name="sample"),
    path('store/', views.store, name="store"),
    path('contact/', views.contact, name="contact"),
]
