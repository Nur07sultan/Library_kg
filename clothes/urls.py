from django.urls import path
from . import views

app_name = 'clothes'

urlpatterns = [
    path('', views.all_clothes, name='all_clothes'),
    path('men/', views.men_clothes, name='men_clothes'),
    path('women/', views.women_clothes, name='women_clothes'),
    path('kids/', views.kids_clothes, name='kids_clothes'),
    path('search/', views.search_clothes, name='search_clothes'),
    path('ajax/', views.clothes_ajax, name='clothes_ajax'),
]





