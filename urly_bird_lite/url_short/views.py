from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response


# Create your views here.
from django.views.generic import ListView, CreateView, View
from url_short.models import UrlBank


def index_view(request):
    return HttpResponse('hello')


class UrlList(ListView):
    model = UrlBank


class UrlCreateView(CreateView):
    model = UrlBank
    fields = ['author', 'body']
    success_url = '/'


class UrlLinkView(View):
    def post(self, request, url_id):
        url = UrlBank.objects.get(id=url_id)
        UrlBank.objects.create(url=url)
        return HttpResponseRedirect(url.url)
