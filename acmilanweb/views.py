from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from acmilanweb.models import Club
from  .forms import ClubForm

def all_clubs(request):
    clubs = Club.objects.all()
    #how_many_teams = len(clubs)
    return render(request, 'clubs.html', {'clubs': clubs,})

def new_club(request):
    form = ClubForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(all_clubs)

    return render(request, 'club_form.html', {'form': form})

def update_club(request, id):
    club = get_object_or_404(Club, pk=id) # Club.object.get(id=id)
    form = ClubForm(request.POST or None, request.FILES or None, instance=club)

    if form.is_valid():
        form.save()
        return redirect(all_clubs)


    return render(request, 'club_form.html', {'form': form})

def delete_club(request, id):
    club = get_object_or_404(Club, pk=id) # Club.object.get(id=id)

    if request.method == "POST":
        club.delete()
        return redirect(all_clubs)

    return render(request, 'confirm_delete.html', {'club': club})