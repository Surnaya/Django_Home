from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.shop, name="shop"),
    path('client/<int:pk>/', views.client_orders, name='client_orders'),
    path('change/<int:pk>/', views.change_client_name, name='change_client_name'),
    path('delete/<int:pk>/', views.delete_client_view, name='delete_client_view'),
]