from django.urls import path

from swengs.homeworkbackend import views

urlpatterns = [
    path('breed', views.breeds_all_create),
    path('breed/<int:pk>', views.breeds_delete_update),
    path('dog', views.dogs_all_create),
    path('dog/<int:pk>', views.dogs_delete_update),
    path('caregiver', views.list_create_caregivers),
]