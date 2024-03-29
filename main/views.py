from django.http import JsonResponse
from rest_framework import generics, permissions
from .models import Box
from .serializers import BoxSerializer, BoxUpdateSerializer
from rest_framework.exceptions import PermissionDenied
from django_filters import rest_framework as django_filters
from .filters import BoxFilter
from django.core.exceptions import ValidationError


class IsStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff


class IsCreatorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user


class CreateBox(generics.CreateAPIView):
    serializer_class = BoxSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaff]

    def perform_create(self, serializer):
        user = self.request.user

        if not user.is_staff:
            raise PermissionDenied(
                "Only Staff members can create a box.")
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=user)

        return JsonResponse({"message": "Box created successfully!"}, status=200)


class BoxUpdate(generics.UpdateAPIView):
    queryset = Box.objects.all()
    serializer_class = BoxUpdateSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaff]


class ListAllBoxes(generics.ListAPIView):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [django_filters.DjangoFilterBackend]
    filterset_class = BoxFilter

    def get_queryset(self):
        if not self.request.user.is_staff:
            return self.queryset.only('length', 'width', 'height')
        return self.queryset


class MyBoxList(generics.ListAPIView):
    serializer_class = BoxSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaff]
    filter_backends = [django_filters.DjangoFilterBackend]
    filterset_class = BoxFilter

    def get_queryset(self):
        user = self.request.user
        return Box.objects.filter(owner=user)


class BoxDelete(generics.DestroyAPIView):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer
    permission_classes = [IsCreatorOrReadOnly]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return JsonResponse({"message": "Box deleted successfully."}, status=200)


def error_404_handler(request, exception):
    return JsonResponse({"message": "page not found!"}, status=404)
