from django.db import models

# Create your models here.
class URLs(models.Model):
    url = models.CharField(max_length=500)
    shorturl = models.CharField(max_length=15, blank=True)
