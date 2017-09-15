# -*- coding: utf-8 -*-

from django import get_version
from django.http import HttpResponse
from django.template import loader
from bs4 import BeautifulSoup

from .articles import descs

from .cards.useless import UselessCard


navbar = loader.get_template('main/navbar.html')
footer = loader.get_template('main/footer.html')
article_box = loader.get_template('articles/description-box.html')


def list_articles(request) :
    context = {
        'bulma_version': '0.4.3',
        'django_version': get_version(),
        'fo_version': '4.7.0',
        'articles': {}
    }

    context['navbar'] = navbar.render(context, request)
    context['footer'] = footer.render(context, request)

    for cat in descs :
        context['articles'].update({descs[cat]['name']: []})
        for art, desc in descs[cat]['articles'].items() :
            desc.update({'id': art, 'category': cat})
            context['articles'][descs[cat]['name']].append(article_box.render(desc))

    index = loader.get_template('articles/list.html')
    return HttpResponse(index.render(context, request))


def read_article(request, category_name, article_name) :
    try :
        description = descs[category_name]['articles'][article_name]
    except KeyError:
        return HttpResponse("The article %s/%s hasn't been referenced" % (category_name, article_name))

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

    # Generate table of contents
    content = BeautifulSoup(context['html'])
    titles = content.find_all(['h2', 'h3'])  # list of titles
    # Extract links informations
    links = []
    for title in titles :
        ide = title.get('id')
        typ = title.name
        txt = title.text
        links.append({
            'id': ide,
            'type': typ,
            'text': txt
        })
    context['titles'] = links

    # Render cards
    for card in description['cards'] :
        context['card_list'].append(card.html(request))

    # Easter egg
    context['card_list'].append(UselessCard().html(request))

    context['navbar'] = navbar.render(context, request)
    context['footer'] = footer.render(context, request)

    index = loader.get_template('articles/index.html')
    return HttpResponse(index.render(context, request))
