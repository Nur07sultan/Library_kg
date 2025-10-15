from django.urls import path
from . import views

app_name = 'clothes'

urlpatterns = [
    path('', views.all_clothes, name='all_clothes'),
    path('ajax/', views.clothes_ajax, name='clothes_ajax'),
]




