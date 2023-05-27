from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.PositiveIntegerField(default=0)
    nickName = models.CharField(max_length=50, blank=True, null=True)


    def __str__(self)-> str:
        return "{} {}".format(self.first_name, self.last_name)

class Pet(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    age = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return "{} - {}".format(self.name, self.person)

class animalSpecies(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    species = models.CharField(max_length=30)

    def __str__(self) -> str:
        return "{} - {}".format(self.species, self.pet)

class Note(models.Model):
    animalSpecies = models.ForeignKey(animalSpecies, on_delete=models.CASCADE)
    note = models.TextField()
    date = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return "{} - {}".format(self.animalSpecies, self.note, self.date)

