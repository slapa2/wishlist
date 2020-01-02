from django.urls import path

from .views import (
    index,
    gifts_list_detail_view,
)

urlpatterns = [
    path('', index, name='landing_page'),
    path('gift_list/<int:pk>', gifts_list_detail_view, name='gifts_list_detail_view'),
]
