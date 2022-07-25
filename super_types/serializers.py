from dataclasses import fields
from rest_framework import serializers
from .models import SuperType


class SuperSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperType
        fields = ['id', 'type']