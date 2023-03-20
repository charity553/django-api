from django.db import models
# CRUD (CREATE, READ, UPDATE, DELETE)


# CREATE
# Create your models here.
class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    # change how you can view drink objects in the admin dashboard from
    # "drink object 1" to grape soda

    # READ
    def __str__(self):
        return self.name + ' ' + self.description
