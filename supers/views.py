from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from super_types.models import SuperType
from super_types.serializers import SuperTypeSerializer
from supers import serializers
from .models import Super
from .serializers import SuperSerializer
from rest_framework import status

@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET':

        super_hero= Super.objects.filter(super_type__type='Hero')
        super_villain = Super.objects.filter(super_type__type='Villain')

        hero_serializer = SuperSerializer(super_hero, many=True)
        villain_serializer = SuperSerializer(super_villain, many=True)

        custom_response_dict = {
            'Heroes': hero_serializer.data,
            'Villains': villain_serializer.data
        }
        return Response(custom_response_dict)

    elif request.method =='POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def super_details(request, pk):
    super = get_object_or_404(Super,pk=pk)
    if request.method == 'GET':
        serializer =SuperSerializer(super)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def super_heroes(request):
    super_type_name = request.query_params.get('type')
    queryset = Super.objects.all()
    if super_type_name:
        queryset = queryset.filter(super_type__type=super_type_name)
    serializer = SuperSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def super_villains(request):
    super_type_name = request.query_params.get('type')
    queryset = Super.objects.all()
    if super_type_name:
        queryset = queryset.filter(super_type__type=super_type_name)
    serializer = SuperSerializer(queryset, many=True)
    return Response(serializer.data)