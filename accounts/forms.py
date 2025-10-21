from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from captcha.fields import CaptchaField

class CustomUserCreationForm(UserCreationForm):
    captcha = CaptchaField()
    
    class Meta:
        model = CustomUser
        fields = [
            'username', 'email', 'first_name', 'last_name', 'middle_name',
            'date_of_birth', 'phone_number', 'city', 'education', 'position_applied',
            'experience_years', 'github_link', 'portfolio_link', 'password1', 'password2'
        ]
        labels = {
            'username': 'Имя пользователя',
            'email': 'Email',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'middle_name': 'Отчество',
            'date_of_birth': 'Дата рождения',
            'phone_number': 'Телефон',
            'city': 'Город',
            'education': 'Образование',
            'position_applied': 'Должность',
            'experience_years': 'Опыт (лет)',
            'github_link': 'GitHub',
            'portfolio_link': 'Портфолио',
            'password1': 'Пароль',
            'password2': 'Подтвердите пароль',
        }

class CustomAuthenticationForm(AuthenticationForm):
    captcha = CaptchaField()


class SimpleCustomUserCreationForm(UserCreationForm):
    """A lightweight user creation form that creates `accounts.CustomUser` but
    does not require a captcha. Use for flows where captcha is undesirable (CineBoard)."""
    class Meta:
        model = CustomUser
        fields = [
            'username', 'email', 'first_name', 'last_name', 'middle_name',
            'date_of_birth', 'phone_number', 'city', 'education', 'position_applied',
            'experience_years', 'github_link', 'portfolio_link', 'password1', 'password2'
        ]
        labels = {
            'username': 'Имя пользователя',
            'email': 'Email',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'middle_name': 'Отчество',
            'date_of_birth': 'Дата рождения',
            'phone_number': 'Телефон',
            'city': 'Город',
            'education': 'Образование',
            'position_applied': 'Должность',
            'experience_years': 'Опыт (лет)',
            'github_link': 'GitHub',
            'portfolio_link': 'Портфолио',
            'password1': 'Пароль',
            'password2': 'Подтвердите пароль',
        }


class MinimalUserCreationForm(UserCreationForm):
    """Minimal registration form: only username and password fields."""
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']
        labels = {
            'username': 'Имя пользователя',
            'password1': 'Пароль',
            'password2': 'Подтвердите пароль',
        }


