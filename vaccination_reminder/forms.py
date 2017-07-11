from django import forms
from django.contrib.auth.models import User
from vaccination_reminder.models import Pets, Vaccinations, VaccinationHistory

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

species = (
    ('0', 'dog'),
    ('1', 'cat'),
)

class PetsForm(forms.ModelForm):
    pet_name = forms.CharField(required=True, help_text="Pet Name")
    species = forms.ChoiceField(choices=species, required=True, help_text="Species")
    birthdate = forms.DateField(required=True, help_text="Date of Birth", widget=forms.TextInput(attrs={'class': 'datepicker'}))

    class Meta:
        model = Pets
        fields = ('pet_name', 'species', 'birthdate', )
