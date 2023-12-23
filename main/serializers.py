from rest_framework import serializers
from .models import Box


class BoxSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(
        source='owner.username', read_only=True)
    area = serializers.SerializerMethodField(
        method_name='get_area', read_only=True)
    volume = serializers.SerializerMethodField(
        method_name='get_volume', read_only=True)

    class Meta:
        model = Box
        fields = ['length', 'breadth', 'height', 'area',
                  'volume', 'created_by', 'created_at', 'updated_at']

    def get_area(self, obj):
        return obj.area

    def get_volume(self, obj):
        return obj.volume

    def __init__(self, *args, **kwargs):
        super(BoxSerializer, self).__init__(*args, **kwargs)

        if not self.context['request'].user.is_staff:
            fields_to_remove = ['created_by', 'created_at', 'updated_at']
            for field in fields_to_remove:
                self.fields.pop(field, None)


class BoxUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = ['length', 'breadth', 'height']
