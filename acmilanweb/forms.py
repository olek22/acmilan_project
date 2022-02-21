from django.forms import ModelForm
from .models import Club

class ClubForm(ModelForm):
    class Meta:
        model = Club
        exclude = ['description']