from django.urls import path
from . import views

urlpatterns = [
	path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
	path('', views.index, name='list'),
	path('deleteall', views.deleteallTask, name='deleteall'),
	path('update/<str:pk>/', views.updateTask, name='update'),
	path('delete/<str:pk>/', views.deleteTask, name='delete'),
]