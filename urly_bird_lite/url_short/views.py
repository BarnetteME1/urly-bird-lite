from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
import hashlib


# Create your views here.
from django.views.generic import ListView, CreateView, View
from url_short.models import UrlBank


def index_view(request):
    context={}
    return render_to_response('base.html', context=context)


class UrlList(ListView):
    model = UrlBank


def shorten_length(self):
    url = self._request.url
    url = bytes(url, encoding="ascii")
    m = hashlib.md5()
    m.update(url)
    return 'localhost:8000/'(m.hexdigest())[:6]


class UrlCreateView(CreateView):
    model = UrlBank
    fields = ['title', 'user', 'url', 'description']
    success_url = '/urls'
    #url = UrlBank.objects.get().filter(id=1)


    def form_valid(self, form):
        model = form.save(commit=False)
        url = bytes(model.url, encoding="ascii")
        m = hashlib.md5()
        m.update(url)
        model.short_url = m.hexdigest()
        return super().form_valid(form)


class UrlLinkView(View):
    def post(self, request, url_id):
        url = UrlBank.objects.get(id=url_id)
        UrlBank.objects.create(user=request.user, url=url)
        return HttpResponseRedirect(url.url)

class GetLinkView(View):

    def get(self, request, url_short):
        url = UrlBank.objects.filter(hash=url_short)
        return HttpResponseRedirect(url.url)