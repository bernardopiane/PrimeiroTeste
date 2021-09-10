from django.db import models


# Create your models here.

# precisa importar Model
class Meetup(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
