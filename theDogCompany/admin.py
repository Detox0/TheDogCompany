# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Persona,Auto,Carnet

# Se registran los modelos creados en la aplicacion para poder administrarlos a traves de /admin
admin.site.register(Persona)
admin.site.register(Auto)
admin.site.register(Carnet)

