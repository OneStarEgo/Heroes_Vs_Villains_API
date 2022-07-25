import re
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SuperType
from .serializers import SuperTypeSerializer
from super_types import serializers
from rest_framework import status

@api_view(['GET', 'POST'])
def super_types_list(request):
    if request.method == 'GET':
        super_types = SuperType.objects.all()
        serializer = SuperTypeSerializer(super_types, many=True)
        return Response(serializer.data)
    elif request.method =='POST':
        serializer = SuperTypeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)