from rest_framework import serializers
from .models import Box


class BoxSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(
        source='owner.username', read_only=True)

    class Meta:
        model = Box
        fields = ['length', 'breadth', 'height', 'area',
                  'volume', 'created_by', 'created_at', 'updated_at']

    def __init__(self, *args, **kwargs):
        super(BoxSerializer, self).__init__(*args, **kwargs)

        if not self.context['request'].user.is_staff:
            fields_to_remove = ['created_by', 'created_at', 'updated_at']
            for field in fields_to_remove:
                self.fields.pop(field, None)


class BoxUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = ['length', 'breadth', 'height',]
