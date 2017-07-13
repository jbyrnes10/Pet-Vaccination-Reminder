from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import Q
from models import Vaccinations, Pets, VaccinationHistory
from datetime import datetime
from vaccination_reminder.forms import PetsForm, AdminForm, VaccineForm

def index(request):
    context_dict = {}
    return render(request, 'vaccination_reminder/index.html', context=context_dict)

def pets(request):
    pets_list = Pets.objects.filter(owner=request.user)

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

def add_vaccine(request, pet_id):
    form = VaccineForm(pet_id)
    pet = Pets.objects.get(id=pet_id)
    form.vaccines.queryset = Vaccinations.objects.filter(species=pet.species) | Vaccinations.objects.filter(species=2)

    if request.method == 'POST':
        form = VaccineForm(pet_id, data=request.POST)
        if form.is_valid():
            vaccine = form.save(commit=False)
            vaccine.pets = pet
            vaccine.save()
            return pet_history(request, pet_id)

        else:
            print(form.errors)

    return render(request, 'vaccination_reminder/add_vaccine.html', {'form': form, 'pet': pet})

def pet_history(request, pet_id):
    pet = Pets.objects.get(id=pet_id)
    vaccinations_history = VaccinationHistory.objects.filter(pets=pet_id)
    vaccinations_list = Vaccinations.objects.filter(species=pet.species) | Vaccinations.objects.filter(species=2)

    context_dict = {'vaccinations_list': vaccinations_list, 'vaccinations_history': vaccinations_history, 'pet': pet}
    return render(request, 'vaccination_reminder/pet_history.html', context=context_dict)

def vaccinations(request):
    vaccination_list = Vaccinations.objects.all()
    context_dict = {'vaccination_list': vaccination_list}
    return render(request, 'vaccination_reminder/vaccinations.html', context=context_dict)

def admin(request):
    form = AdminForm()
    if request.method == 'POST':
        form = AdminForm(request.POST)

        if form.is_valid():
            pet = form.save(commit=True)
            pet.save()
            return admin(request)

        else:
            print(form.errors)

    return render(request, 'vaccination_reminder/admin.html', {'form': form})

def admin_search_pets(request):
    if request.method == 'POST':
        owner_id = request.POST.get('owner')
        pets_list = Pets.objects.all().filter(owner=owner_id)

    return render_to_response('vaccination_reminder/admin_search_pets.html', {'results': pets_list, }, context_instance=RequestContext(request))