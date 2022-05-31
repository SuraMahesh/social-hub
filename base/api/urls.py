from .import views
from django.urls import path

urlpatterns = [
    path('', views.getRoutes),
    path('api/posts/', views.getPosts),
    path('api/posts/add/', views.addPost),
    path('api/posts/edit/<str:pk>/', views.editPost),
    path('api/posts/<str:pk>/', views.getPost),
    path('api/users/', views.getUsers),
    path('api/users/recommended', views.getRecommendedUsers),
    path('api/users/<str:username>/', views.getUser),
    path('api/company/', views.getCompanies),
    path('api/company/<str:pk>/', views.getCompany),
    path('api/jobs/', views.getJobs),
]