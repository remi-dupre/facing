from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^article/(?P<article_name>(?:\d|\w|-|_)+)/$', views.read_article, name='read_article')
]
