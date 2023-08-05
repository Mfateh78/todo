from django.urls import path 
from . import views
from .views import LoginView

urlpatterns = [
    path('login/', views.loginpage, name='login'),
    path('register/', views.registerpage, name='register'),
    path('logout/', views.logoutuser, name='logout'),

    path('', views.home, name='home'),

    path('create/', views.createtask, name='create'),
    path('update/<str:pk>/', views.updatetask, name='update'),
    path('delete/<str:pk>/', views.deletetask, name='delete'),
]
