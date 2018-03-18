# restaurantes/views.py

from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from random import randint
from .models import restaurantes_c
import math
from .forms import RestauranteForm, ModificarForm, AniadirForm
from django.contrib.auth.decorators import login_required

def consulta_pagina_numero(pagina, busqueda, tipo):
    restaurante=restaurantes_c.find({"borough": busqueda})

    #Obtengo los contenidos en función del número de paginación
    inicio=int(pagina)*20
    final=int(pagina)*20+20
    restaurante=restaurante[inicio:final]

    restaurantes=[]

    for item in restaurante:
        restaurantes.append({'name': item["name"],'borough': item["borough"],'cuisine': item["cuisine"]})

    resultado=JsonResponse(restaurantes,safe=False)

    return resultado

def consulta_grafico():
    pipe = [{"$group": {"_id": "$cuisine", "count": {"$sum": 1}}}]
    restaurante=restaurantes_c.aggregate(pipeline=pipe)

    cocinas=[]

    for item in restaurante:
        cocinas.append({'cuisine': item["_id"],'count': item["count"]})

    resultado=JsonResponse(cocinas,safe=False)

    return resultado

def index(request):
    context = {}
    return render(request,'base.html', context)

def svg(request):
    opcion=randint(0,4)
    context = {
        'opcion': opcion
    }
    return render(request,'svg.html', context)

@login_required
def restaurantes(request):
    if request.method == "POST":
        tipo=""
        busqueda=""
        restaurante={}
        tope=0
        form = RestauranteForm(request.POST)
        if form.is_valid():
            tipo="barrio"
            busqueda=form.cleaned_data['borough']
            restaurante=restaurantes_c.find({"borough": busqueda})
            
            tope=math.ceil(restaurante.count()/20)
            restaurante=restaurante[:20]

            context = {
                'tipo': tipo,
                'busqueda': busqueda,
                'respuesta': restaurante,
                'tope': tope
            }
            return render(request,'restaurantes-resultado.html', context)
    else:
        form = RestauranteForm()
        context = {'form': form}
        return render(request,'restaurantes.html', context)

@login_required
def modificarrestaurante(request):
    if request.method == "POST":
        ident = ""
        nombre = ""
        barrio = ""
        cocina = ""
        lat = ""
        lon = ""
        form = ModificarForm(request.POST)
        if form.is_valid():
            ident = form.cleaned_data['ident']
            nombre = form.cleaned_data['name']
            barrio = form.cleaned_data['borough']
            cocina = form.cleaned_data['cuisine']
            lat = form.cleaned_data['lat']
            lon = form.cleaned_data['lon']

            #Modifico la información del restaurante
            restaurantes_c.update_one(
                {'restaurant_id':ident},
                {'$set': {"restaurant_id": ident, "name": nombre, "borough": barrio, "cuisine": cocina}},
                upsert=False
            )
            
            context = {
                'ident': ident,
                'nombre': nombre,
                'barrio': barrio,
                'cocina': cocina,
                'lat': lat,
                'lon': lon,
                'form': form
            }
            return render(request,'modificar-restaurante.html', context)

    else:
        ident = request.GET['id']
        nombre = request.GET['nombre']
        barrio = request.GET['barrio']
        cocina = request.GET['cocina']
        lat = request.GET['lat']
        lon = request.GET['lon']
        form = ModificarForm(initial={'ident':ident ,'name': nombre, 'borough': barrio, 'cuisine': cocina, 'lat': lat, 'lon': lon})

        context = {'ident': ident, 'nombre': nombre, 'barrio': barrio, 'cocina': cocina, 'lat': lat, 'lon': lon, 'form': form}
        return render(request,'modificar-restaurante.html', context)

@login_required
def aniadirrestaurante(request):
    if request.method == "POST":
        nombre = ""
        barrio = ""
        cocina = ""
        cp = ""
        form = AniadirForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['name']
            barrio = form.cleaned_data['borough']
            cocina = form.cleaned_data['cuisine']
            cp = form.cleaned_data['zipcode']

            #Modifico la información del restaurante
            restaurantes_c.insert(
               {
                  "address" : {
                     "street" : "Pintor Yañez",
                     "zipcode" : cp,
                     "building" : "1313",
                     "coord" : [ -73.9557413, 40.7720266 ]
                  },
                  "borough" : barrio,
                  "cuisine" : cocina,
                  "grades" : [],
                  "name" : nombre,
                  "restaurant_id" : "41704620"
               }
            )

            restaurante=restaurantes_c.find({"name": nombre})
            
            context = {
                'respuesta': restaurante,
            }
            return render(request,'aniadir-restaurante.html', context)
        else:
            context = {'form': form}
            return render(request,'aniadir-restaurante.html', context)

    else:
        form = AniadirForm(initial={'name': 'Restaurante Miguel', 'borough': 'Almedina', 'cuisine': 'Española', 'zipcode': 0})

        context = {'form': form}
        return render(request,'aniadir-restaurante.html', context)

def getpagina(request):
    pagina = request.GET['pagina']
    busqueda = request.GET['busqueda']
    tipo = request.GET['tipo']
    restaurantes = consulta_pagina_numero(pagina, busqueda, tipo)
    return restaurantes

def getgrafico(request):
    grafico = consulta_grafico()
    return grafico