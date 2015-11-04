import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
import hashlib
import random


# Create your views here.
from django.views.generic import ListView, CreateView, View
from url_short.models import UrlBank, ClickCount
from numpy import unicode
from rest_framework.authentication import BasicAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class UrlList(ListView):
    model = UrlBank

class UrlUserList(ListView):
    model = UrlBank

    def get_queryset(self):
        user = self.kwargs.get('pk')
        return self.model.objects.filter(user__id=user)


class UrlCreateView(CreateView):
    model = UrlBank
    fields = ['title', 'url', 'description']
    success_url = '/'

    def form_valid(self, form):
        model = form.save(commit=False)
        model.user = self.request.user
        urllink = ("{}{}{}".format(model.url, model.user, datetime.datetime.now().strftime("%f")))
        urllink = bytes(urllink, encoding="ascii")
        m = hashlib.md5()
        m.update(urllink)
        model.short = (m.hexdigest())[:random.randint(5, 9)]
        return super().form_valid(form)


class UrlLinkView(View):

    def post(self, request, url_id):
        url = UrlBank.objects.get(id=url_id)
        UrlBank.objects.create(user=request.user, url=url)
        return HttpResponseRedirect(url.url)


class GetLinkView(View):

    def get(self, request, short):
        shorts = short
        urlitem = UrlBank.objects.get(short=shorts)
        return HttpResponseRedirect(urlitem.url)

    def post(self, request, short):
        shorts = short
        urlitem = UrlBank.objects.get(short=shorts)
        ClickCount.objects.create(link=urlitem, user=request.user)
        return HttpResponseRedirect(urlitem.url)


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url ='/'

class AuthView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated)

    def get(self, request, format=None):
        content = {
            'user': unicode(request.user),
            'auth': unicode(request.auth),
        }
        return Response(content)