from django.db import models


class Book(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.name
