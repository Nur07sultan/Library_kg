from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.book_list_view, name='book_list'),
    path('book_detail/<int:id>/', views.book_detail_view, name='book_detail'),
    path('book_detail/<int:id>/episode/<int:episode_id>/', views.book_detail_view, name='book_episode'),
    path('time/', views.current_time, name='current_time'),
    path('random/', views.random_number, name='random_number'),
    path('about_me/', views.about_me, name='about_me'),
]



