from django.urls import path
from gym import views



urlpatterns = [
    path('', views.index, name='index'),
]
