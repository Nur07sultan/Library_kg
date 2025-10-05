from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list_view, name='books_list'),
    path('book_detail/<int:pk>/', views.book_detail_view, name='book_detail'),
    path('time/', views.current_time, name='current_time'),
    path('random/', views.random_number, name='random_number'),
    path('about_me/', views.about_me, name='about_me'),
]