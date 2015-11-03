from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
import hashlib
import random


# Create your views here.
from django.views.generic import ListView, CreateView, View
from url_short.models import UrlBank


def index_view(request):
    context={}
    return render_to_response('base.html', context=context)


class UrlList(ListView):
    model = UrlBank


class UrlCreateView(CreateView):
    model = UrlBank
    fields = ['title', 'user', 'url', 'description']
    success_url = '/urls'

    def form_valid(self, form):
        model = form.save(commit=False)
        url = bytes(model.url, encoding="ascii")
        m = hashlib.md5()
        m.update(url)
        model.short = (m.hexdigest())[:random.randint(5, 9)]
        return super().form_valid(form)


class UrlLinkView(View):


    def post(self, request, url_id):
        url = UrlBank.objects.get(id=url_id)
        UrlBank.objects.create(user=request.user, url=url)
        return HttpResponseRedirect(url.url)


class GetLinkView(View):

    def get(self, request, short):
        short = short[:-1]
        url = UrlBank.objects.get(short=short)
        return HttpResponseRedirect(url.url)