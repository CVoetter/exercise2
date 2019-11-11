from rest_framework import serializers
from . import models


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Breed
        fields = ['breed_name', 'fci_number']


class DogSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Dog
        fields = ['name', 'arrival_date', 'breed_name', 'caregiver']


class CaregiverSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Caregiver
        fields = ['first_name', 'last_name']
