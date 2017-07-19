# -*- coding: utf-8 -*-

from django import get_version
from django.http import HttpResponse
from django.template import loader

from .articles import descs as article_descs

from .cards.useless import UselessCard


navbar = loader.get_template('main/navbar.html')
footer = loader.get_template('main/footer.html')
article_box = loader.get_template('articles/description-box.html')


def list_articles(request) :
    context = {
        'bulma_version': '0.4.3',
        'django_version': get_version(),
        'fo_version': '4.7.0',
        'articles': []
    }

    context['navbar'] = navbar.render(context, request)
    context['footer'] = footer.render(context, request)

    for art, desc in article_descs.items() :
        desc.update({'id': art})
        context['articles'].append(article_box.render(desc))

    index = loader.get_template('articles/list.html')
    return HttpResponse(index.render(context, request))


def read_article(request, article_name) :
    try :
        description = article_descs[article_name]
    except KeyError:
        return HttpResponse("The article %s hasn't been referenced" % article_name)

    context = {
        'title': description['title'],
        'description': description['description'],
        'html': description['html'],
        'date': description['date'],
        'card_list': [],
        'bulma_version': '0.4.3',
        'django_version': get_version(),
        'fo_version': '4.7.0'
    }

    # Render cards
    for card in description['cards'] :
        context['card_list'].append(card.html(request))

    # Easter egg
    context['card_list'].append(UselessCard().html(request))

    context['navbar'] = navbar.render(context, request)
    context['footer'] = footer.render(context, request)

    index = loader.get_template('articles/index.html')
    return HttpResponse(index.render(context, request))
