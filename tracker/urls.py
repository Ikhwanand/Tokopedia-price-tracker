from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home_view, name='home-view'),
    path('delete/<int:pk>', views.delete_link, name='delete-link'),
]
