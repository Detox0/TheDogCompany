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
