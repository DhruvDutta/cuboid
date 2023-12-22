from rest_framework import viewsets
from .models import Box
from .serializers import BoxSerializer, EmployeeSerializer
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Employee, Box
from .decorators import token_required, staff_only
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from rest_framework import generics
from rest_framework import filters
from .models import Box
from .serializers import BoxSerializer


@staff_only
@require_POST
def create_box(request, user):
    if request.method == 'POST':
        length = request.POST.get('length')
        breadth = request.POST.get('breadth')
        height = request.POST.get('height')
        if not all([length, breadth, height]):
            return JsonResponse({"error": "Incomplete data provided."}, status=400)
        try:
            length = float(length)
            breadth = float(breadth)
            height = float(height)
        except ValueError:
            return JsonResponse({"error": "Invalid numeric values provided."}, status=400)

        box = Box.objects.create(
            length=length, breadth=breadth, height=height, employee=user.employee)
        box.save()
        print(box.area)
        return JsonResponse({"message": f"Box Created Successfully"}, status=200)
    return JsonResponse({"message": f"create a post request!"}, status=400)


@staff_only
def update_box(request, user, box_id):
    try:
        box = Box.objects.get(id=box_id, employee=user.employee)
    except Box.DoesNotExist:
        return JsonResponse({"message": "Box not found or does not belong to the user."}, status=404)

    length = request.POST.get('length')
    breadth = request.POST.get('breadth')
    height = request.POST.get('height')

    if not all([length, breadth, height]):
        return JsonResponse({"error": "Incomplete data provided."}, status=400)

    try:
        length = float(length)
        breadth = float(breadth)
        height = float(height)
    except ValueError:
        return JsonResponse({"error": "Invalid numeric values provided."}, status=400)

    # Update the Box
    box.length = length
    box.breadth = breadth
    box.height = height
    box.save()

    # Print the updated area
    print(box.area)

    return JsonResponse({"message": f"Box updated successfully."}, status=200)


@token_required
def list_boxes(request, user):
    if user.is_staff:
        # If the user is staff, include additional information (Created By and Last Updated)
        boxes_data = [
            {
                "id": box.id,
                "length": box.length,
                "width": box.breadth,
                "height": box.height,
                "area": box.area,
                "volume": box.volume,
                "created_by": box.employee.user.username,
                "last_updated": box.updated_at,
            }
            for box in Box.objects.all()
        ]
    else:
        # If the user is not staff, exclude Created By and Last Updated
        boxes_data = [
            {
                "id": box.id,
                "length": box.length,
                "width": box.breadth,
                "height": box.height,
                "area": box.area,
                "volume": box.volume,
            }
            for box in Box.objects.all()
        ]

    return JsonResponse({"boxes": boxes_data}, status=200)


class BoxList(generics.ListCreateAPIView):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['length', 'breadth',
                       'height', 'created_at', 'updated_at']
    search_fields = ['length', 'breadth', 'height', 'created_at', 'updated_at']


class BoxDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer
