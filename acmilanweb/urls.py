from django.contrib import admin
from django.urls import path
from .views import all_clubs, new_club, update_club, delete_club,main, gallery, anthem, trivia


urlpatterns = [
    path('', main, name="main"),
    path('gallery/', gallery, name="gallery"),
    path('seriea_clubs/', all_clubs, name="all_clubs"),
    path('trivia/', trivia, name="trivia"),
    path('anthem/', anthem, name="anthem"),
    path('seriea_clubs/create', new_club, name="create_club"),
    path('seriea_clubs/update/<int:id>/', update_club, name="update_club"),
    path('seriea_clubs/delete/<int:id>/', delete_club, name="delete_club"),
]
