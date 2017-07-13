import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'vaccination_reminder.settings')

import django
django.setup()
from vaccination_reminder.models import User, Vaccinations, Pets, VaccinationHistory

def populate():
    vaccine_list = [
        {"vaccination_name":"Rabies",
         "species":2,
         "first_shot_age_months":4,
         "second_shot_age_months":16,
         "third_shot_age_months":None,
         "fourth_shot_age_months":None,
         "vaccination_frequency_years":3,
         "description":"Rabies is a virus affecting the brain and spinal cord, passed by the saliva of a diseased animal through bites or scratches. There is no cure and it is always fatal. "
                       "It is preventable through vaccination. The first shot can be given between 4-6 months of age (sometimes sooner), the second given a year later, "
                       "and every three years after (this is a fairly new development; vaccines used to be yearly)."},
        {"vaccination_name":"Canine Distemper",
         "species":0,
         "first_shot_age_months":2,
         "second_shot_age_months":3,
         "third_shot_age_months":4,
         "fourth_shot_age_months":16,
         "vaccination_frequency_years":3,
         "description": "Distemper is a contagious virus spread through direct or indirect contact with an infected animal. "
                        "There is no cure, so vaccination is important for prevention. As a puppy, this is part of a series of vaccines starting around 2 months of age."},
        {"vaccination_name":"Canine Parvovirus - DHPP",
         "species":0,
         "first_shot_age_months":2,
         "second_shot_age_months":3,
         "third_shot_age_months":4,
         "fourth_shot_age_months":16,
         "vaccination_frequency_years":1,
         "description":"Parvovirus is a highly contagious virus that can be fatal, especially in young puppies. Vaccination is dramatically reducing the number of cases."},
        {"vaccination_name":"Adenovirus-2 (Hepatitis)",
         "species":0,
         "first_shot_age_months":2,
         "second_shot_age_months":3,
         "third_shot_age_months":4,
         "fourth_shot_age_months":16,
         "vaccination_frequency_years":3,
         "description":"Adenovirus Type 2 is related to the Hepatitis virus (Adenovirus-1). Adenovirus-2 is one of the causes of Tracheobronchitis, aka Kennel Cough. "
                       "Shelter animals are especially at risk of infection because it is spread through direct contact with an infected dog or through contaminated feces or urine."},
        {"vaccination_name": "Herpesvirus (Rhinotracheitis)",
         "species":1,
         "first_shot_age_months":2,
         "second_shot_age_months":3,
         "third_shot_age_months":4,
         "fourth_shot_age_months":16,
         "vaccination_frequency_years":3,
         "description": "Feline Herpes is a virus spread through contact with an infected cat's eyes, mouth or nose. It can also be transferred by cats that share litter boxes or food and water dishes."
                        "It is highly contagious and cats can even be carriers without ever displaying symptoms."},
        {"vaccination_name": "Calicivirus",
         "species":1,
         "first_shot_age_months":2,
         "second_shot_age_months":3,
         "third_shot_age_months":4,
         "fourth_shot_age_months":16,
         "vaccination_frequency_years":3,
         "description":"Calicivirus is a common respiratory disease in cats. It is spread easily to non-vaccinated cats, especially in shelters."},
        {"vaccination_name":"Feline Panleukopenia (Distemper)",
         "species":1,
         "first_shot_age_months":2,
         "second_shot_age_months":3,
         "third_shot_age_months":4,
         "fourth_shot_age_months":16,
         "vaccination_frequency_years":3,
         "description": "Distemper is present in most environments, so cats are always exposed to it, making vaccinations important. "
                        "It can be fatal in kittens, and was once the leading cause of death in cats before the vaccine was common."},
    ]

    for vacs in vaccine_list:
        add_vaccine(vacs["vaccination_name"],
                    vacs["species"],
                    vacs["first_shot_age_months"],
                    vacs["second_shot_age_months"],
                    vacs["third_shot_age_months"],
                    vacs["fourth_shot_age_months"],
                    vacs["vaccination_frequency_years"],
                    vacs["description"])

def add_vaccine(vaccination_name, species, first_shot_age_months, second_shot_age_months, third_shot_age_months, fourth_shot_age_months, vaccination_frequency_years, description):
    v = Vaccinations.objects.get_or_create(vaccination_name=vaccination_name, species=species, first_shot_age_months=first_shot_age_months, second_shot_age_months=second_shot_age_months,
                                           third_shot_age_months=third_shot_age_months, fourth_shot_age_months=fourth_shot_age_months, vaccination_frequency_years=vaccination_frequency_years, description=description)[0]
    v.save()
    return v

if __name__ == '__main__':
    print("Starting Pet Vaccination Reminder population script...")
    populate()