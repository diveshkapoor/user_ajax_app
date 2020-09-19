from django.contrib import admin
from django.urls import include, path
from app1.views import create_user, get_user_all, get_user_id, update_user, user_delete


urlpatterns = [
    #path('view/<int:user_id_pk>/', get_user_id),
    path('view/', get_user_all),
    path('add/', create_user, name='add value'),
    path('detail_view/<int:user_id_pk>/', get_user_id,name='detail_view'),
    path('edit/<int:user_id_pk>/', update_user, name='edit'),
    path('view/delete/', user_delete, name='user_delete'),
]
