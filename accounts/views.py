# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib import messages

# ===== Регистрация =====
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # сразу логиним пользователя
            messages.success(request, f"Добро пожаловать, {user.first_name}!")
            return redirect('books:book_list')  # <- после регистрации редирект на список книг
        else:
            # Если форма невалидна, ошибки покажутся в шаблоне
            return render(request, 'accounts/register.html', {'form': form})
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

# ===== Логин =====
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Вы вошли как {user.first_name} {user.last_name}")
            return redirect('books:book_list')  # редирект после успешного входа
        else:
            return render(request, 'accounts/login.html', {'form': form})
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# ===== Логаут =====
def logout_view(request):
    logout(request)
    messages.info(request, "Вы вышли из аккаунта")
    return redirect('books:book_list')







