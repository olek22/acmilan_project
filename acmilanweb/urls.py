from django.contrib import admin
from django.urls import path
from .views import all_clubs, new_club, update_club, delete_club,main, gallery, anthem, trivia, register, user, delete_user, info_club
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', main, name="main"),

    path('user/', user, name="user"),
    path('user/delete_user/', delete_user, name="delete_user"),
    path('register/', register, name="register"),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='reset_password/reset_password.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='reset_password/password_reset_sent.html'), name='password_reset_done'),
    path('reset_password_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='reset_password/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='reset_password/reset_password_complete.html'), name='password_reset_complete'),

    path('gallery/', gallery, name="gallery"),
    path('trivia/', trivia, name="trivia"),
    path('anthem/', anthem, name="anthem"),

    path('seriea_clubs/', all_clubs, name="all_clubs"),
    path('seriea_clubs/create', new_club, name="create_club"),
    path('seriea_clubs/info/<int:id>/', info_club, name="info_club"),
    path('seriea_clubs/update/<int:id>/', update_club, name="update_club"),
    path('seriea_clubs/delete/<int:id>/', delete_club, name="delete_club"),
]
