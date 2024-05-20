from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.shop, name="shop"),
    path('clients/', views.all_clients, name='all_clients'),
    path('client/<int:pk>/', views.client_orders_view, name='client_orders_view'),
    path('change/<int:pk>/', views.change_client_name, name='change_client_name'),
    path('delete/<int:pk>/', views.delete_client_view, name='delete_client_view'),
    path('client/<int:pk>/orders/', views.ordered_products, name='ordered_products'),

]