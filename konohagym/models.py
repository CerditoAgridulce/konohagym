from django.db import models

# Create your models here.

class Muscle(models.Model):
    name = models.CharField(max_length=300, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripción", blank=True, null=True)
    image = models.ImageField(upload_to='muscles', blank=True)
    
    def __str__(self):
        return self.name
    
class Excercise(models.Model):
    name = models.CharField(max_length=300, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripción", blank=True, null=True)
    image = models.ImageField(upload_to='excercises', verbose_name="Ejemplo", blank=True)
    muscles = models.ManyToManyField(Muscle, verbose_name="Músculos")
    
    def __str__(self):
        return self.name 
