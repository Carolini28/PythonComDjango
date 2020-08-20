from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name='accounts'
urlpatterns = [
	path('entrar/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
	path('sair/', auth_views.LogoutView.as_view(next_page='core:home'), name='logout'),
	path('cadastre-se/', views.register, name='register'),
]