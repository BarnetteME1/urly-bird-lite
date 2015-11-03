from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.serializers import ModelSerializer
from url_short.models import UrlBank, ClickCount


class UrlSerializer(ModelSerializer):

    class Meta:
        model = UrlBank


class UrlListView(ListCreateAPIView):
    queryset = UrlBank.objects.all()
    serializer_class = UrlSerializer


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
