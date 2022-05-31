from .import views
from django.urls import path

urlpatterns = [
    path('', views.getRoutes),
    path('api/posts/', views.getPosts),
    path('api/users/', views.getUsers)
]