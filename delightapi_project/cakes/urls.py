from django.urls import path
from .views import get_all_cakes, cake_list_view

urlpatterns = [
    path('', get_all_cakes, name='cake-api'),
    path('page/', cake_list_view, name='cake-html'),
]
