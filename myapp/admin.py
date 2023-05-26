from django.contrib import admin
from myapp.models import Person, Pet, animalSpecies, Note

# Register your models here.

admin.site.register(Person)
admin.site.register(Pet)
admin.site.register(animalSpecies)
admin.site.register(Note)


