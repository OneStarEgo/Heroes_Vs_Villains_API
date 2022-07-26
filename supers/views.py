from rest_framework.decorators import api_view
from rest_framework.response import Response
from supers import serializers
from .models import Super
from .serializers import SuperSerializer
from rest_framework import status

@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET':
        supers = Super.objects.all()
        serializer = SuperSerializer(supers, many=True)
        return Response(serializer.data)
    elif request.method =='POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)