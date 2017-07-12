from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from vaccination_reminder import views
from registration.backends.simple.views import RegistrationView
from django.contrib.auth.views import password_change, password_change_done

class UserRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return '/vaccination_reminder/'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/register/$', UserRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/password/change/$', password_change,
      {'template_name': 'registration/password_change_form.html'},
      name='password_change'),
    url(r'^accounts/password/change/done/$', password_change_done,
      {'template_name': 'registration/password_change_done.html'},
      name='password_change_done'),
    url(r'^vaccinations/$', views.vaccinations, name='vaccinations'),
    url(r'^pets/$', views.pets, name='pets'),
    url(r'^add_pet/$', views.add_pet, name='add_pet'),
    url(r'^add_vaccine/(?P<pet_id>[0-9]+)', views.add_vaccine, name='add_vaccine'),
    url(r'^pet_history/(?P<pet_id>[0-9]+)', views.pet_history, name='pet_history'),
    url(r'^admin/$', views.admin, name='admin'),
    url(r'^admin_search_pets/$', views.admin_search_pets, name='admin_search_pets'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
