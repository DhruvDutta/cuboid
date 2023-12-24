from django.db.models import F
from django_filters import rest_framework as filters
from rest_framework import generics, permissions
from .models import Box
from .serializers import BoxSerializer


class BoxFilter(filters.FilterSet):
    length__gt = filters.NumberFilter(field_name='length', lookup_expr='gt')
    length__lt = filters.NumberFilter(field_name='length', lookup_expr='lt')
    width__gt = filters.NumberFilter(field_name='width', lookup_expr='gt')
    width__lt = filters.NumberFilter(field_name='width', lookup_expr='lt')
    height__gt = filters.NumberFilter(field_name='height', lookup_expr='gt')
    height__lt = filters.NumberFilter(field_name='height', lookup_expr='lt')
    area__gt = filters.NumberFilter(field_name='area', lookup_expr='gt')
    area__lt = filters.NumberFilter(field_name='area', lookup_expr='lt')
    volume__gt = filters.NumberFilter(field_name='volume', lookup_expr='gt')
    volume__lt = filters.NumberFilter(field_name='volume', lookup_expr='lt')
    created_at__gt = filters.DateTimeFilter(
        field_name='created_at', lookup_expr='gt')
    created_at__lt = filters.DateTimeFilter(
        field_name='created_at', lookup_expr='lt')

    created_by__username = filters.CharFilter(
        field_name='owner__username', lookup_expr='exact')

    class Meta:
        model = Box
        fields = ['length', 'width', 'height', 'created_at']
