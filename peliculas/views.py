from django.shortcuts import render

# Create your views here.

from .models import Genero, Pelicula, Director

def index(request):
    num_pelicula = Pelicula.objects.all().count()
    num_director = Director.objects.all().count()
    num_genero = Genero.objects.all().count()


    return render(
        request,
        'index.html',
        context={
            'num_pelicula': num_pelicula,
            'num_director': num_director,
            'num_genero': num_genero
        }
    )
