from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import ModelSerializer
from url_short.models import UrlBank, ClickCount


class UrlSerializer(ModelSerializer):

    class Meta:
        model = UrlBank
        fields = ('title', 'url', 'description', 'short', 'created')


class UrlListView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = UrlBank.objects.all()
    serializer_class = UrlSerializer

    def get_queryset(self):
        user = self.request.user.id
        return UrlBank.objects.filter(user=user)


class UrlDetailView(RetrieveUpdateDestroyAPIView):
    queryset = UrlBank.objects.all()
    serializer_class = UrlSerializer


class CountSerializer(ModelSerializer):

    class Meta:
        model = ClickCount


class CountListView(ListCreateAPIView):
    queryset = ClickCount.objects.all()
    serializer_class = CountSerializer


class CountDetailView(RetrieveUpdateDestroyAPIView):
    queryset = ClickCount.objects.all()
    serializer_class = UrlSerializer