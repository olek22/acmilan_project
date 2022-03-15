from django.forms import ModelForm, EmailField, CharField, DateField, TextInput, NumberInput
from django.contrib.auth.models import User
# from django.contrib.admin.widgets import SelectDateWidget
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Club, Profile
from datetime import date


class ClubForm(ModelForm):
    class Meta:
        model = Club
        exclude = ['description']


class ExtendedUserCreationForm(UserCreationForm):
    email = EmailField(required=True)
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=30)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('location', 'date_of_birth')

    years = [x for x in range(1900, date.today().year)]

    date_of_birth = DateField(widget=NumberInput(attrs={'type': 'date'}), required=False)


class EditProfileForm(UserChangeForm):
    email = EmailField(required=True, widget=TextInput(attrs={'class': 'form-control'}))
    first_name = CharField(max_length=30, widget=TextInput(attrs={'class': 'form-control'}))
    last_name = CharField(max_length=30, widget=TextInput(attrs={'class': 'form-control'}))
    username = CharField(max_length=30, widget=TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        # exclude = []
        fields = ('username', 'first_name', 'last_name', 'email')

class EditInfoForm(ProfileForm):
    location = CharField(max_length=30, widget=TextInput(attrs={'class': 'form-control'}))
    date_of_birth = DateField(widget=NumberInput(attrs={'type': 'date'}), required=False)

    class Meta:
        model = User
        fields = ('date_of_birth', 'location')