from django.urls import path

from . import views

urlpatterns = [
    path('1', views.index, name='1'),
    path('2', views.index1, name='2'),
]