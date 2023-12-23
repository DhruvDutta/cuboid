from django.db.models import F
from django_filters import rest_framework as filters
from rest_framework import generics, permissions
from .models import Box
from .serializers import BoxSerializer


class BoxFilter(filters.FilterSet):
    length__gt = filters.NumberFilter(field_name='length', lookup_expr='gt')
    length__lt = filters.NumberFilter(field_name='length', lookup_expr='lt')
    breadth__gt = filters.NumberFilter(field_name='breadth', lookup_expr='gt')
    breadth__lt = filters.NumberFilter(field_name='breadth', lookup_expr='lt')
    height__gt = filters.NumberFilter(field_name='height', lookup_expr='gt')
    height__lt = filters.NumberFilter(field_name='height', lookup_expr='lt')
    area__gt = filters.NumberFilter(method='filter_area_gt')
    area__lt = filters.NumberFilter(method='filter_area_lt')
    volume__gt = filters.NumberFilter(method='filter_volume_gt')
    volume__lt = filters.NumberFilter(method='filter_volume_lt')
    created_at__gt = filters.DateTimeFilter(
        field_name='created_at', lookup_expr='gt')
    created_at__lt = filters.DateTimeFilter(
        field_name='created_at', lookup_expr='lt')

    created_by__username = filters.CharFilter(
        field_name='owner__username', lookup_expr='exact')

    class Meta:
        model = Box
        fields = ['length', 'breadth', 'height', 'created_at']

    def filter_area_gt(self, queryset, name, value):
        return queryset.filter(length__gt=0, breadth__gt=0).annotate(
            area=F('length') * F('breadth')).filter(area__gt=value)

    def filter_area_lt(self, queryset, name, value):
        return queryset.filter(length__gt=0, breadth__gt=0).annotate(
            area=F('length') * F('breadth')).filter(area__lt=value)

    def filter_volume_gt(self, queryset, name, value):
        return queryset.filter(length__gt=0, breadth__gt=0, height__gt=0).annotate(
            volume=F('length') * F('breadth') * F('height')).filter(volume__gt=value)

    def filter_volume_lt(self, queryset, name, value):
        return queryset.filter(length__gt=0, breadth__gt=0, height__gt=0).annotate(
            volume=F('length') * F('breadth') * F('height')).filter(volume__lt=value)
