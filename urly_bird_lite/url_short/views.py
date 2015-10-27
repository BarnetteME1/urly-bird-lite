from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response


# Create your views here.
from django.views.generic import ListView
from url_short.models import UrlBank


def index_view(request):
    return HttpResponse('hello')


class UrlList(ListView):
    model = UrlBank
    template_name = 'base.html'
