from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_order),
    path('<int:pk>/', views.order_detail),
    path('member/', views.list_orders_by_member),
]