from django.urls import path

from .views import (
    gifts_list_create_view,
    gifts_list_detail_view,

    gift_create_view,
    gift_detail_view,
    gift_update_view,
    gift_delete_view,
)

urlpatterns = [
    path('gifts_list_create', gifts_list_create_view, name='gifts_list_create_view'),
    path('gifts_list/<int:pk>', gifts_list_detail_view, name='gifts_list_detail_view'),

    path('gifts_list/<int:gifts_list_pk>/gift_create', gift_create_view, name='gift_create_view'),

    path('gift/<int:gift_pk>/detail', gift_detail_view, name='gift_detail_view'),
    path('gift/<int:gift_pk>/update', gift_update_view, name='gift_update_view'),
    path('gift/<int:gift_pk>/delete', gift_delete_view, name='gift_delete_view'),
]
