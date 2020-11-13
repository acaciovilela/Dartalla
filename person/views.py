from django.shortcuts import render
from django.views.generic import ListView


class ListPersonView(ListView):
    model = Person
