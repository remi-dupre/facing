# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        r'^article/(?P<category_name>(?:\d|\w|-|_)+)/(?P<article_name>(?:\d|\w|-|_)+)/$',
        views.read_article, name='read_article'
    ),
    url(
        r'^article/',
        views.list_articles, name='list_articles'
    )
]
