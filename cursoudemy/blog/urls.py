from django.urls import path
from . import views

urlpatterns = [
    # path del blog
    path('blog/', views.blog, name="blog"),
    path('category/<int:category_id>/', views.category, name="category"),
]