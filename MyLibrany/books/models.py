from django.db import models

class Autor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

class Book(models.Model):
    name = models.CharField(max_lenght=100)
    description  = models.CharField(max_lenght=500)
    on_stock = models.BooleanField(default=True)
    category = models.ManyToManyField(Category)
    autor = models.ManyToManyField(Autor)




