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
        fields = ('pet_name', 'species', 'birthdate')

class VaccineForm(forms.ModelForm):
    vaccines = Vaccinations.objects.all()
    vaccinations = forms.ModelChoiceField(queryset=vaccines, required=True, help_text="Vaccine")
    date_vaccinated = forms.DateField(required=True, help_text="Date Vaccinated",
                                widget=forms.TextInput(attrs={'class': 'datepicker'}))

    class Meta:
        model = VaccinationHistory
        fields = ('vaccinations', 'date_vaccinated')

    def __init__(self, pet_id, *args, **kwargs):
        super(VaccineForm, self).__init__(**kwargs)
        pet = Pets.objects.get(id=pet_id)
        self.fields['vaccinations'].queryset = Vaccinations.objects.filter(species=pet.species) | Vaccinations.objects.filter(species=2)


class AdminForm(forms.ModelForm):
    owners = User.objects.all()
    owner = forms.ModelChoiceField(queryset=owners, required=True, help_text="Owner's User ID")

    class Meta:
        model = Pets
        fields = ('owner',)
