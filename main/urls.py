from django.urls import path
from .views import CreateBox, MyBoxList, BoxDelete, ListAllBoxes, BoxUpdate

urlpatterns = [
    path('list_boxes/', ListAllBoxes.as_view(), name='box-list'),
    path('create/', CreateBox.as_view(), name='box-create'),
    path('update/<int:pk>/', BoxUpdate.as_view(), name='box-update'),

    path('my_boxes/', MyBoxList.as_view(), name='my-box-list'),
    path('delete_box/<int:pk>/', BoxDelete.as_view(), name='box-delete'),
    # ... other URL patterns ...
]
