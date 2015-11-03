from django.contrib import admin

# Register your models here.
from url_short.models import UrlBank, ClickCount

admin.site.register(UrlBank)
admin.site.register(ClickCount)