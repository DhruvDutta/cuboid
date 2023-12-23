from django.http import JsonResponse
from django.views.decorators.http import require_POST
from rest_framework import generics
from rest_framework import permissions
from rest_framework import filters
from .models import Box
from .serializers import BoxSerializer, BoxUpdateSerializer
from rest_framework.exceptions import PermissionDenied
from django_filters import rest_framework as django_filters
from .filters import BoxFilter


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

        # Check if the user is staff
        if user.is_staff:
            serializer.save(owner=user)
        else:
            # Non-staff user is not allowed to create a box
            raise PermissionDenied(
                "You do not have permission to create a box.")


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
            return self.queryset.only('length', 'breadth', 'height')
        return self.queryset


class MyBoxList(generics.ListAPIView):
    serializer_class = BoxSerializer
    permission_classes = [permissions.AllowAny]
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
