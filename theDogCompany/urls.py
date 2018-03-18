from django.conf.urls import url
from . import views

# URL's que pueden ser visitadas, cada una produce un efecto distinto
# para revisar que hace cada una, revisar funcion llamada, ej: views.crear_persona (funcion 'crear_persona' en archivo 'views')

urlpatterns = [
    url(r'^$', views.index),
    url(r'^personas/crear$',views.crear_persona),
    url(r'^autos/crear$',views.crear_auto),
    url(r'^carnet/crear$',views.crear_carnet),

    url(r'^personas/todas$',views.personas_todas),
    url(r'^autos/todos$',views.autos_todos),
    url(r'^carnet/todos$',views.carnet_todos),

    url(r'^personas/eliminar/(?P<pk>[0-9]+)$',views.eliminar_persona),
    url(r'^autos/persona/(?P<pk>[0-9]+)$',views.autos_persona),

]