from django.shortcuts import render
from django.db import connection
from .models import *



# Create your views here.
def show_accueil(request):
    jeux = list.objects.all()

    return render(request, 'accueil/home.html', {'nom_table':jeux})

def list_bdd_tables():
    tables = connection.introspection.table_names()
    seen_models = connection.introspection.installed_models(tables)
    new_name= []

    for name in tables:
        name = str(name)
        boolean = exclusion_case(name)
        if boolean == True:
            nouveau_nom = name.split("accueil_")
            new_name.append(nouveau_nom)
    return new_name

def exclusion_case(nom):
    if 'auth' in nom:
        return False
    else:
        if 'django' in nom:
            return False
        else:
            if nom == "":
                return False
            return True