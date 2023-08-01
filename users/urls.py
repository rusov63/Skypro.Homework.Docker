from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import ProfileView, UserRegisterView, EmailConfirmationSentView, UserConfirmEmailView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'), # войти
    path('logout/', LogoutView.as_view(), name='logout'), # выйти
    path('register/', UserRegisterView.as_view(), name='register'), # регистрация
    path('profile/', ProfileView.as_view(), name='profile'), # профиль
]