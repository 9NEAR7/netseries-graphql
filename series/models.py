from django.db import models

# Create your models here.

class Serie(models.Model):
    name = models.TextField() 
    description = models.TextField(blank=True)
    year = models.TextField()
    seasons = models.TextField()
    url = models.URLField()
    
