from django.urls import path
from . import views, telegramViews
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('register_user/', views.register_user, name='register_user'),
    path('profile/', views.profile, name='profile'),

    path('remove_user', views.remove_user, name="remove_user"),

    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('edit_email/', views.edit_email, name='edit_email'),

]