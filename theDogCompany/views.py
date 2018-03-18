# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# Vista inicial, para que no se vea tan vacia la pagina
def index(request):
    return HttpResponse('<h1>¡Bienvenido! (por ahora) la pagina funciona.')

###### FUNCIONES QUE LEEN DATOS #######

#Funcion que entrega a todas las personas registradas en la BD
def personas_todas(request):

    if (request.method == 'GET'):

        # Se consulta por todas las personas y se les pasan a serializer
        personas = Persona.objects.all()
        serializer = PersonaSerializer(personas,many=True)

        # Se retornan todos los objetos encontrados con formato JSON
        return JsonResponse(serializer.data, safe=False)


# Funcion que entrega a todos los autos registradas en la BD
def autos_todos(request):

   if (request.method == 'GET'):

        # Se consulta por todos los autos y se les pasan a serializer
        autos = Auto.objects.all()
        serializer = AutoSerializer(autos, many=True)

        # Se retornan todos los objetos encontrados con formato JSON
        return JsonResponse(serializer.data, safe=False)

# Funcion que entrega a todas las personas registradas en la BD
def carnet_todos(request):

    if (request.method == 'GET'):
        # Se consulta por todas las personas y se les pasan a serializer
        carnet = Carnet.objects.all()
        serializer = CarnetSerializer(carnet, many=True)

        # Se retornan todos los objetos encontrados con formato JSON
        return JsonResponse(serializer.data, safe=False)


# Funcion que entrega los autos asociados a una persona
def autos_persona(request,pk):

    if(request.method == 'GET'):

        # Buscamos los autos que posee una persona en especifico (con el id)
        autos = Auto.objects.filter(persona__id=pk)
        serializer = AutoSerializer(autos,many=True)

        return JsonResponse(serializer.data, safe=False)

###### FUNCIONES QUE CREAN DATOS #######

# Funcion para crear una persona
@csrf_exempt
def crear_persona(request):

    # Nos aseguramos de que el metodo de ingreso sea un metodo POST
    if(request.method == 'POST'):

        # Se reciben los datos y se les entregan al serializer
        data = JSONParser().parse(request)
        serializer = PersonaSerializer(data=data)

        # Se verifican los datos
        if serializer.is_valid():
            serializer.save()

            #Se guardan los datos y se le entrega un mensaje 'created'
            return JsonResponse(serializer.data, status=201)

        # En caso contrario 'Bad request'
        return JsonResponse(serializer.errors, status=400)


# Funcion para crear un auto
@csrf_exempt
def crear_auto(request):

    # Nos aseguramos de que el metodo de ingreso sea un metodo POST
    if(request.method == 'POST'):

        # Se reciben los datos y se les entregan al serializer
        data = JSONParser().parse(request)
        serializer = AutoSerializer(data=data)

        # Se verifican los datos
        if serializer.is_valid():
            serializer.save()

            #Se guardan los datos y se le entrega un mensaje 'created'
            return JsonResponse(serializer.data, status=201)

        # En caso contrario 'Bad request'
        return JsonResponse(serializer.errors, status=400)

# Funcion para crear un carnet
@csrf_exempt
def crear_carnet(request):

    # Nos aseguramos de que el metodo de ingreso sea un metodo POST
    if(request.method == 'POST'):

        # Se reciben los datos y se les entregan al serializer
        data = JSONParser().parse(request)
        serializer = CarnetSerializer(data=data)

        # Se verifican los datos
        if serializer.is_valid():
            serializer.save()

            #Se guardan los datos y se le entrega un mensaje 'created'
            return JsonResponse(serializer.data, status=201)

        # En caso contrario 'Bad request'
        return JsonResponse(serializer.errors, status=400)



###### FUNCIONES QUE BORRAN DATOS #######

# Funcion que puede eliminar una persona registrada en la base de datos a traves de su ID
def eliminar_persona(request,pk):

    if (request.method == 'GET'):

        persona = Persona.objects.get(pk=pk)

        persona.delete()

        return HttpResponse('<h2>OK</h2>')

