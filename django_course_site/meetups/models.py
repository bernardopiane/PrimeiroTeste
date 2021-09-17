from django.db import models


# Create your models here.

# precisa importar Model
class Meetup(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to="images")

    # pagina admin mostra como nome a string do modelo
    def __str__(self):
        return f'{self.title} - {self.slug}'
