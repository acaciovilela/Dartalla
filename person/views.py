from django.views.generic import ListView

from person.models import Person


class ListPersonView(ListView):
    model = Person
