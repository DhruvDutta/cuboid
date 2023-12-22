from rest_framework import serializers
from .models import Box
from django.contrib.auth.models import User
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['position']


class UserSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(many=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'employee']


class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = '__all__'
