from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UrlBank(models.Model):
    title = models.CharField(max_length=25, blank=True)
    url = models.CharField(max_length=150, blank=True)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User)
    short = models.CharField(max_length=32, blank=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
        unique_together = ('url', 'user')

    @property
    def count(self):
        clicker = ClickCount.objects.filter(link=self)
        return clicker.count()


class ClickCount(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    link = models.ForeignKey(UrlBank)
    clicked = models.DateTimeField(auto_now_add=True)