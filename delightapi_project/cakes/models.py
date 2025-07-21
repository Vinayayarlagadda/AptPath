from django.db import models
from django.contrib.postgres.fields import ArrayField

class Cake(models.Model):
    cakeId = models.AutoField(primary_key=True)
    cakeName = models.CharField(max_length=100)
    cakeDescription = models.TextField()
    cakeFlavour = models.CharField(max_length=50)
    cakeImage = models.ImageField(upload_to='cake_images/')
    cakeTags = ArrayField(models.CharField(max_length=30), blank=True, default=list)
    cakeIngredients = ArrayField(models.CharField(max_length=100), blank=True, default=list)
    cakeEggOptions = ArrayField(models.CharField(max_length=10), blank=True, default=list)

    def __str__(self):
        return self.cakeName