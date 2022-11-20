from django.shortcuts import render, get_object_or_404
from .models import Animal

def animal_list(request):
    animals = Animal.objects.all()
    return render(request, 'animalerie/animal_list.html', {"animals" : animals})