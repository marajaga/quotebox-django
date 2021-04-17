from django.db import models
from django_random_queryset import RandomManager

class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=200)
    contributor =  models.CharField(max_length=200)
    published = models.BooleanField(default=False)
    objects = RandomManager()
