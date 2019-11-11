from django.db import models


class Breed(models.Model):

    breed_name = models.TextField()
    fci_number = models.PositiveIntegerField()

    def __str__(self): return self.breed_name


class Dog(models.Model):

    name = models.TextField()
    arrival_date = models.DateField()
    breed_name = models.ForeignKey(Breed, on_delete=models.CASCADE)
    caregiver = models.ManyToManyField('Caregiver')

    def __str__(self): return self.name


class Caregiver(models.Model):

    first_name = models.TextField()
    last_name = models.TextField()

    def __str__(self): return self.last_name

