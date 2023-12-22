from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Employee
from functools import wraps
from django.contrib.auth.decorators import login_required


def token_required(function):
    @wraps(function)
    @csrf_exempt
    def wrap(request, *args, **kwargs):
        if "api-key" in request.headers and len(request.headers.get("api-key")) > 0:
            token = request.headers.get("api-key")
            try:
                employee = Employee.objects.get(token=token)
                user = employee.user
                # user.last_login = timezone.now()
                # user.save(update_fields=['last_login'])
                # if user.is_designer:
                #    return JsonResponse({"message": "Designer does not have access to this function"})
            except (Employee.DoesNotExist,):
                return JsonResponse({"message": "Token not match"}, status=403)
            return function(request, user, *args, **kwargs)
        else:
            return JsonResponse({"message": "Token not found"}, status=401)
    return wrap


def staff_only(function):
    @wraps(function)
    @csrf_exempt
    @token_required
    def wrap(request, *args, **kwargs):
        token = request.headers.get("api-key")
        employee = Employee.objects.get(token=token)
        user = employee.user
        if not user.is_staff:
            return JsonResponse({"message": "User is not staff"}, status=400)
        return function(request, *args, **kwargs)
    return wrap
