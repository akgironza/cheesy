from django.db import models

# Create your models here.

class Cheese(models.Model):
    name = models.CharField(max_length=100)
    origin_country = models.CharField(max_length=100)
    type = models.CharField(max_length=100)