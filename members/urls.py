from django.urls import path
from . import views

urlpatterns = [
    path('', views.members),
    path('<int:pk>/', views.members_detail),
]