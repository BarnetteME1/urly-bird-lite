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
from url_short.views import index_view, UrlList, UrlCreateView, UrlLinkView, GetLinkView

urlpatterns = [
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^$', index_view),
    url(r'^urls/$', UrlList.as_view(), name='url_list'),
    url(r'^create/$', login_required(UrlCreateView.as_view()), name='url_create'),
    url(r'^urllink/(?P<url_id>\d+)/$', UrlLinkView.as_view(), name="url_link"),
   #url(r'^c/(?P<bookmark_shortcut>.+)/$', ClickShortcut.as_view(), name="click_shortcut"),
    url(r'^r/(?P<short>.+/$)', GetLinkView.as_view(), name='short_url'),
    url(r'^admin/', include(admin.site.urls)),
]
