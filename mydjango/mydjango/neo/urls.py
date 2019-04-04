from django.urls import path

from .views import (
    neo_create_view,
    neo_create_id_view,
    neo_delete_id_view,
    neo_list_view,
)

app_name = 'neo'
urlpatterns = [
    path('', neo_create_view, name='neo_create'),
    path('<int:my_id>/', neo_create_id_view, name='neo_create_id'),
    path('<int:my_id>/delete/', neo_delete_id_view, name='neo_delete_id'),
    path('list/', neo_list_view, name='neo_list'),
]

