from django.contrib.auth import login, logout
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, View
from .forms import CustomUserCreationForm, CustomAuthenticationForm


class RegisterView(FormView):
    template_name = 'accounts/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('books:book_list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, f"Добро пожаловать, {user.first_name}!")
        return super().form_valid(form)


register_view = RegisterView.as_view()


class LoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = CustomAuthenticationForm
    success_url = reverse_lazy('books:book_list')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        messages.success(self.request, f"Вы вошли как {user.first_name} {user.last_name}")
        return super().form_valid(form)


login_view = LoginView.as_view()


class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.info(request, "Вы вышли из аккаунта")
        return redirect('books:book_list')


logout_view = LogoutView.as_view()







