from django.urls import path
from . import views

app_name = 'basket'

urlpatterns = [
    path('', views.OrderListView.as_view(), name='order_list'),
    path('add/', views.OrderCreateView.as_view(), name='order_add'),
    path('edit/<int:pk>/', views.OrderUpdateView.as_view(), name='order_edit'),
    path('delete/<int:pk>/', views.OrderDeleteView.as_view(), name='order_delete'),
]
