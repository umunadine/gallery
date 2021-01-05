from django.db import models
import datetime as dt

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length =50)

