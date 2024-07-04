from django.urls import path
from . import views

urlpatterns = [
    path('', views.items),
    path('<int:pk>/', views.items_detail),
]