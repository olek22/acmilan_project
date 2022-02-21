from django.contrib import admin
from django.urls import path
from .views import all_clubs, new_club, update_club, delete_club


urlpatterns = [
    path('seriea_clubs/', all_clubs),
    path('seriea_clubs/create', new_club),
    path('seriea_clubs/update/<int:id>/', update_club),
    path('seriea_clubs/delete/<int:id>/', delete_club),
]
