from django.shortcuts import render, get_object_or_404, redirect
from acmilanweb.models import Club, Profile
from .forms import ClubForm, ExtendedUserCreationForm, ProfileForm, EditProfileForm, EditInfoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.models import User
from django.views import generic
from django.urls import reverse_lazy

def main(request):
    return render(request, 'main.html')


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('main')


def info_club(request, id):
    club = get_object_or_404(Club, pk=id)
    club_dict = {x: y for (x, y) in club.__dict__.items() if len(str(y)) > 0}
    photo = club_dict['club_crest']
    del club_dict['id'], club_dict['_state'], club_dict['club_crest']
    club_info = [(k.capitalize().replace('_', ' '),v) for k,v in club_dict.items()]
    # print(club_info)
    # print(photo)


    return render(request, 'club_info.html', {'club_info': club_info, 'club':club, 'photo':photo})

def all_clubs(request):
    clubs = Club.objects.all()
    return render(request, 'clubs.html', {'clubs': clubs})

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

            profile = profile_form.save(commit=False) # commit=False -> bez wysyłania do bazy danych
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


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile_page.html'
    success_url = reverse_lazy('user')

    def get_object(self):
        return self.request.user

class ProfileEditView(generic.UpdateView):
    form_class = EditInfoForm
    template_name = 'registration/edit_profile_info.html'
    success_url = reverse_lazy('user')

    def get_object(self):
        return self.request.user.profile




def gallery(request):
    return render(request, 'gallery.html')

@login_required
def user(request):
    return render(request, 'user.html')

@login_required
def delete_user(request):
    current_user = request.user.id
    user = get_object_or_404(User, pk=current_user)
    print(user)
    user.delete()

    return redirect(main)
