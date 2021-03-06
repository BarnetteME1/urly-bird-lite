"""urly_bird_lite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from url_short.views import UrlList, UrlCreateView, UrlLinkView, GetLinkView, UserCreateView, UrlUserList, UserList
from rest_framework.authtoken import views

urlpatterns = [
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^api/', include('urly_api.urls')),
    url(r'^users/$', UserList.as_view(), name='user_list'),
    url(r'^$', UrlList.as_view(), name='url_list'),
    url(r'^(?P<pk>\d+)/$', UrlUserList.as_view(), name='user_list'),
    url(r'^create_user/$', UserCreateView.as_view(), name='user_create'),
    url(r'^create/$', login_required(UrlCreateView.as_view()), name='url_create'),
    url(r'^url_link/(?P<url_id>\d+)/$', UrlLinkView.as_view(), name='url_link'),
    url(r'^Shr\.tn/(?P<short>.+)/$', GetLinkView.as_view(), name='short_url'),
    url(r'^admin/', include(admin.site.urls)),
]
