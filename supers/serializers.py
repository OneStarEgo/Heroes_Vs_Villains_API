from dataclasses import fields
from rest_framework import serializers
from .models import Super



class SuperSerializer(serializers.ModelSerializer):
    super_type = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Super
        fields = ['id', 'name', 'alter_ego', 'primary_ability', 'secondary_ability', 'catchphrase', 'super_type_id']
        depth = 1