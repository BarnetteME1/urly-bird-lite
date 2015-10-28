from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UrlBank(models.Model):
    title = models.CharField(max_length=25, blank=True)
    url = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User)
    short_url = models.CharField(max_length=50, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
        unique_together = ('url', 'user')