from django.db import models

# Create your models here.


class UrlBank(models.Model):
    url = models.TextField()
    description = models.TextField(blank=True)