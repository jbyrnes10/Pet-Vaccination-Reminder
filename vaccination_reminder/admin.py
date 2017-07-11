from django.contrib import admin
from vaccination_reminder.models import Vaccinations, VaccinationHistory, Pets

admin.site.register(Vaccinations)
admin.site.register(VaccinationHistory)
admin.site.register(Pets)