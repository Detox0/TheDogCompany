# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Modelos a utilizar dentro de la aplicacion, existen tres: persona, auto y carnet

class Persona(models.Model):

    nombre = models.CharField(max_length=50)
    apellidoPaterno = models.CharField(max_length=50)
    apellidoMaterno = models.CharField(max_length=50)
    edad = models.IntegerField(default=0)

    #Necesario para que cuando se pregunte por el objeto retorne el valor indicado
    def __str__(self):
        return self.nombre


class Auto(models.Model):

    modelo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    patente = models.CharField(max_length=10,blank=True)
    anio = models.IntegerField()

    #Llave foranea para indicar que el auto pertenece a una persona en especifico
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE,blank=True)

    # Necesario para que cuando se pregunte por el objeto retorne el valor indicado
    def __str__(self):
        return self.marca

class Carnet(models.Model):

    fechaVencimiento = models.DateField()
    numeroSerie = models.CharField(max_length=10)
    activo = models.BooleanField(blank=False,null=False)
    persona = models.OneToOneField(Persona,on_delete=models.CASCADE)

    # Necesario para que cuando se pregunte por el objeto retorne el valor indicado
    def __str__(self):
        return self.numeroSerie