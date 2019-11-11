from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from swengs.homeworkbackend.serializers import BreedSerializer, DogSerializer, CaregiverSerializer
from . import models


@api_view(['GET', 'POST'])
def breeds_all_create(request):

    if request.method == 'GET':
        breeds = models.Breed.objects.all()
        serializer = BreedSerializer(breeds, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BreedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', 'PUT', 'GET'])
def breeds_delete_update(request, pk):
    try:
        breed = models.Breed.objects.get(pk=pk)
    except models.Breed.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        breed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = BreedSerializer(breed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        serializer = BreedSerializer(breed)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def dogs_all_create(request):

    if request.method == 'GET':
        dogs = models.Dog.objects.all()
        serializer = DogSerializer(dogs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', 'PUT', 'GET'])
def dogs_delete_update(request, pk):
    try:
        dog = models.Dog.objects.get(pk=pk)
    except models.Dog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        dog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = DogSerializer(dog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        serializer = DogSerializer(dog)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def list_create_caregivers(request):
    if request.method == 'GET':
        caregivers = models.Caregiver.objects.all()
        serializer = CaregiverSerializer(caregivers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CaregiverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
