from django.urls import path
from . import views

app_name = 'cineboard'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('channels/', views.ChannelListView.as_view(), name='channels'),
    path('item/<int:id>/', views.ItemDetailView.as_view(), name='item_detail'),
    # Movies
    path('movies/', views.MovieListView.as_view(), name='movie_list'),
    path('movies/add/', views.MovieCreateView.as_view(), name='movie_add'),
    path('movies/<int:id>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('movies/<int:id>/edit/', views.MovieUpdateView.as_view(), name='movie_edit'),
    path('movies/<int:id>/delete/', views.MovieDeleteView.as_view(), name='movie_delete'),

    # Auth
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
