from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import Q
from models import Vaccinations, Pets, VaccinationHistory
from datetime import datetime
from vaccination_reminder.forms import PetsForm

def index(request):
    context_dict = {}
    return render(request, 'vaccination_reminder/index.html', context=context_dict)

def pets(request):
    pets_list = Pets.objects.filter(owner=request.user)

    #vaccination_list = VaccinationHistory.objects.filter(pets_list)
    #'vaccination_list': vaccination_list
    context_dict = {'pets_list': pets_list}
    return render(request, 'vaccination_reminder/pets.html', context=context_dict)

def add_pet(request):
    form = PetsForm()
    if request.method == 'POST':
        form = PetsForm(request.POST)

        if form.is_valid():
            pet = form.save(commit=True)
            pet.owner = request.user
            pet.save()
            return pets(request)

        else:
            print(form.errors)

    return render(request, 'vaccination_reminder/add_pet.html', {'form': form})

def pet_history(request, pet_id):
    vaccinations_list = VaccinationHistory.objects.filter(pets=pet_id)

    #vaccination_list = VaccinationHistory.objects.filter(pets_list)
    #'vaccination_list': vaccination_list
    context_dict = {'vaccinations_list': vaccinations_list}
    return render(request, 'vaccination_reminder/pet_history.html', context=context_dict)


def vaccinations(request):
    #vaccination_list = Vaccinations.objects.filter(species=) filter by species of animal clicked on
    context_dict = {}
    return render(request, 'vaccination_reminder/vaccinations.html', context=context_dict)

def admin(request):

    context_dict = {}
    return render(request, 'vaccination_reminder/admin.html', context=context_dict)