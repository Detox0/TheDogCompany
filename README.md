# Prueba de concepto para The Dog Company

Repositorio donde se encuentra la prueba de concepto desarrollada para The DogCompany, se ha creado un modelo de una persona, un auto y un carnet, entre la persona y el carnet existe una relación 1 es 1 y entre la persona y el auto una relación de 1 es a N.

Para hacer funcionar el proyecto, se debe descargar (o clonar) el repositorio de GitHub y dentro de él, correr el siguiente comando `python manage.py runserver`luego ingresar en la direccion creada. Las consultas disponibles se pueden acceder con las siguientes URL's:

* ~/personas/crear -> Recibe un JSON con la estructura del modelo `Persona`y lo guarda en la BD.
* ~/autos/crear -> Recibe un JSON con la estructura del modelo `Auto`y lo guarda en la BD.
* ~/carnet/crear -> Recibe un JSON con la estructura del modelo `Carnet`y lo guarda en la BD.
* ~/personas/todas -> Entrega todas las personas guardadas en la BD
* ~/autos/todos -> Entrega todos los autos guardados en la BD
* ~/carnet/todos -> Entrega todos los carnet guardadas en la BD
* ~/personas/eliminar/(id_persona) -> Elimina una persona de la BD
* ~/autos/persona/(id_persona) ->Entrega todos los autos de una persona guardadas en la BD
