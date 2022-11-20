from .models import Animal, Equipement

def changeLieu(animal, nouveauLieu):
    message = ''

    lieu = nouveauLieu.id_equip
    libre = nouveauLieu.disponibilite == "libre"
    if lieu == "litiere" and animal.etat != "endormi":
        return "Désolé, " + animal.id_animal + " ne dort pas !"
    if not libre:
        return "Désolé, la" + lieu + " est déjà occupé."
    
    if lieu == "nid" and animal.etat != "fatigue":
        message = "Désolé, le" + animal.id_animal + " n'est pas fatigué !"
    if lieu == "roue" and animal.etat != "repus":
        message = "Désolé, la" + animal.id_animal + " n'est pas en état de faire du sport !"
    if lieu == "mangeoire" and animal.etat != "affame":
        message = "Désolé, la" + animal.id_animal + " n'a pas faim !"
    
    return message

def majEtat(animal, prochainLieu):
    lieu = prochainLieu.id_equip
    if lieu == "litiere":
        animal.etat = "affame"
    if lieu == "nid":
        animal.etat = "endormi"
    if lieu == "roue":
        animal.etat = "fatigue"
    if lieu == "mangeoire":
        animal.etat = "repus"