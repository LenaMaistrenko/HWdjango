from django.urls import path
from . import views

urlpatterns = [
    path('', views.headphone_info, name='headphone_info'),
]