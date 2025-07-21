from django.db import models

# Create your models here.

class place_order(models.Model):
    name = models.CharField(max_length=100)
    product = models.CharField(max_length=100)


class cancel_order(models.Model):
    name = models.CharField(max_length=100)
    product = models.CharField(max_length=100)