from django.contrib.auth.models import User
from django.db import models
import hashlib
import random

# Create your models here.


class UrlBank(models.Model):
    title = models.CharField(max_length=25, blank=True)
    url = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User)
    short_url = models.CharField(max_length=50, blank=True)

    @property
    def shorten_length(self):
        url = self.url
        url = bytes(url, encoding="ascii")
        m = hashlib.md5()
        m.update(url)
        return (m.hexdigest())[:random.randint(5, 32)]

    def __str__(self):
        return self.title

