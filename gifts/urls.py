from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_gifts_list, name='gift_list'),
]
