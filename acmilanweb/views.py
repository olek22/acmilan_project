from django.shortcuts import render
from django.http import HttpResponse
from acmilanweb.models import Club

def all_clubs(request):
    clubs = Club.objects.all()
    #how_many_teams = len(clubs)
    return render(request, 'clubs.html', {'clubs': clubs,})