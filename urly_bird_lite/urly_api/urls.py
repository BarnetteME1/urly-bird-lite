from django import views
from django.conf.urls import include, url
from urly_api.views import UrlListView, UrlDetailView, CountListView, CountDetailView

urlpatterns = [
    url(r'^urls/$', UrlListView.as_view(), name='url_api_list'),
    url(r'^urls/(?P<pk>\d+)/$', UrlDetailView.as_view(), name='url_api_detail'),
    url(r'^clicks/$', CountListView.as_view(), name='count_api_list'),
    url(r'^clicks/(?P<pk>\d+)/$', CountDetailView.as_view(), name='count_api_detail'),
]
