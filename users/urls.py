from django.urls import path

from .views import (
    home_page_view
)

urlpatterns = [
    path('home_page', home_page_view, name='user_home_page_view'),
]
