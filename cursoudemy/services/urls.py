from django.urls import path
from . import views

urlpatterns = [
    # path del core
    path('services/', views.services, name="services"),
]