from django.db import models

# Create your models here.

class Funko(models.Model):
    name = models.CharField(max_length=128)
    number = models.IntegerField()
    collection = models.CharField(max_length=128)
    is_backlight = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.number} - {self.name}'

class User(models.Model):
    name = models.CharField(max_length=128)
    funkos = models.ManyToManyField(Funko, blank=True)

    def __str__(self):
        return self.name

#-------------------------------------------------------------

class Movie(models.Model):
    title = models.CharField(max_length=128)
    director = models.CharField(max_length=128)
    age = models.IntegerField()
    genre = models.CharField(max_length=128)
    
    def __str__(self):
        return f'{self.title} - {self.director}'

class Actor(models.Model):
    name = models.CharField(max_length=128)
    movies = models.ManyToManyField(Movie, blank=True)

    def __str__(self):
        return self.name