from django.urls import path

from .views import (
    gifts_list_create_view,
    gifts_list_detail_view,
)

urlpatterns = [
    path('gifts_list_create', gifts_list_create_view, name='landing_page'),
    path('gifts_list/<int:pk>', gifts_list_detail_view, name='gifts_list_detail_view'),
]
