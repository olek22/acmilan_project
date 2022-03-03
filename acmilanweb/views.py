from django.shortcuts import render, get_object_or_404, redirect
from acmilanweb.models import Club, Profile
from .forms import ClubForm, ExtendedUserCreationForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

def main(request):
    return render(request, 'main.html')

def all_clubs(request):
    clubs = Club.objects.all()
    #how_many_teams = len(clubs)
    return render(request, 'clubs.html', {'clubs': clubs,})

def trivia(request):
    return render(request, 'trivia.html')

def anthem(request):
    return render(request, 'anthem.html')

@login_required
def new_club(request):
    form = ClubForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(all_clubs)

    return render(request, 'club_form.html', {'form': form})

@login_required
def update_club(request, id):
    club = get_object_or_404(Club, pk=id) # Club.object.get(id=id)
    form = ClubForm(request.POST or None, request.FILES or None, instance=club)

    if form.is_valid():
        form.save()
        return redirect(all_clubs)


    return render(request, 'club_form.html', {'form': form})

@login_required
def delete_club(request, id):
    club = get_object_or_404(Club, pk=id) # Club.object.get(id=id)

    if request.method == "POST":
        club.delete()
        return redirect(all_clubs)

    return render(request, 'confirm_delete.html', {'club': club})

def register(request):

    if request.method == "POST":
        form = ExtendedUserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, password=password, username=username)
            login(request, user)
            return redirect(main)
    else:
        form = ExtendedUserCreationForm()
        profile_form = ProfileForm()

    return render(request, 'registration/register.html', {'form' : form, 'profile_form': profile_form})


def gallery(request):
    return render(request, 'gallery.html')

@login_required
def user(request):
    return render(request, 'user.html')