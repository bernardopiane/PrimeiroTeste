from django.db import models


# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name}'


# precisa importar Model
class Meetup(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to="images")
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    # pagina admin mostra como nome a string do modelo
    def __str__(self):
        return f'{self.title} - {self.slug}'
