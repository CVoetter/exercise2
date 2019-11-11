from django.contrib import admin
from . import models


class CaregiverAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Caregiver, CaregiverAdmin)


class DogAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Dog, DogAdmin)


class BreedAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Breed, BreedAdmin)