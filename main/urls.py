from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import create_box, update_box, list_boxes, BoxList, BoxDetail


urlpatterns = [
    path('add/', create_box, name='create'),
    path('update/<int:box_id>/', update_box, name='update'),
    path('list/', list_boxes, name='list'),
    path('list_boxes/', BoxList.as_view(), name='box-list'),
]
