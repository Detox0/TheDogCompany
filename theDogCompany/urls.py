from django.conf.urls import url
from . import views

# URL's que pueden ser visitadas, cada una produce un efecto distinto
# para revisar que hace cada una, revisar funcion llamada, ej: views.crear_persona (funcion 'crear_persona' en archivo 'views')

urlpatterns = [
    url(r'^$', views.index),
    url(r'^crear/persona$',views.crear_persona),
    url(r'^crear/auto$',views.crear_auto),
    url(r'^crear/carnet',views.crear_carnet),
]