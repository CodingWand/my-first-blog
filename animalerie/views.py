from django.shortcuts import render, get_object_or_404, redirect
from .forms import MoveForm
from .models import Animal, Equipement
from .controleur import changeLieu, majEtat

def animal_list(request):
    animals = Animal.objects.all()
    return render(request, 'animalerie/animal_list.html', {'animals': animals})

def animal_detail(request, id_animal, message=""):
    animal = get_object_or_404(Animal, id_animal=id_animal)
    
    if request.method == "POST":
        form = MoveForm(request.POST, instance=animal)
    else:
        form = MoveForm()
    
    if form.is_valid():
        ancien_lieu = get_object_or_404(Equipement, id_equip=animal.lieu.id_equip)
        
        form.save(commit=False)
        nouveau_lieu = get_object_or_404(Equipement, id_equip=animal.lieu.id_equip)
        message = changeLieu(animal, nouveauLieu=nouveau_lieu)

        if message != "":
            return redirect('animal_detail_mes', id_animal=id_animal, message=message)

        ancien_lieu.disponibilite = "libre"
        ancien_lieu.save()
        
        nouveau_lieu.disponibilite = "occupé"
        nouveau_lieu.save()

        majEtat(animal=animal, prochainLieu=nouveau_lieu)
        animal.save()

        return redirect('animal_detail', id_animal=id_animal)
    
    return render(request,
                  'animalerie/animal_detail.html',
                  {'animal': animal, 'lieu': animal.lieu, 'form': form, 'message': message})