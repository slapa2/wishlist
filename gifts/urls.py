from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_gifts_list, name='gift_list'),
    path('get_gift/<int:id>/', views.get_gift, name='get_gift')
]
