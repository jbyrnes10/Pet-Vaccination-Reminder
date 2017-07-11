from django.db import models
from django.contrib.auth.models import User

class Vaccinations(models.Model):
    vaccination_name = models.CharField(max_length=50, null=False)
    species_list = (
        (0, 'dog_only'),
        (1, 'cat_only'),
        (2, 'both_species'),
    )
    species = models.PositiveSmallIntegerField(choices=species_list)
    first_shot_age_months = models.PositiveSmallIntegerField(default=0)
    second_shot_age_months = models.PositiveSmallIntegerField(null=True)
    third_shot_age_months = models.PositiveSmallIntegerField(null=True)
    fourth_shot_age_months = models.PositiveSmallIntegerField(null=True)
    vaccination_frequency_years = models.PositiveSmallIntegerField(default=0)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self

class Pets(models.Model):
    pet_name = models.CharField(max_length=20, null=False)
    birthdate = models.DateField(null=False)
    owner = models.ForeignKey(User, related_name='owner')

    species_list = (
        (0, 'dog'),
        (1, 'cat'),
    )
    species = models.PositiveSmallIntegerField(choices=species_list)

    def save(self, *args, **kwargs):
        super(Pets, self).save(*args, **kwargs)

    def __str__(self):
        return self

class VaccinationHistory(models.Model):
    pets = models.ForeignKey(Pets, related_name='pets')
    vaccinations = models.ForeignKey(Vaccinations, related_name='vaccinations')
    date_vaccinated = models.DateField(null=False)
    date_due = models.DateField()

    def __str__(self):
        return self