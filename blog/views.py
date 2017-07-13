from django.http import HttpResponse
from django.template import loader

from .articles import descs as article_descs

from .cards.github import GithubCard
from .cards.useless import UselessCard


def read_article(request, article_name) :
    try :
        description = article_descs[article_name]
    except KeyError:
        return HttpResponse("The article %s hasn't been referenced" % article_name)

    context = {
        'title': description['title'],
        'description': description['description'],
        'html': description['html'],
        'card_list': []
    }

    # Render cards
    for card in description['cards'] :
        context['card_list'].append(card.html(request))

    # Easter egg
    context['card_list'].append(UselessCard().html(request))

    navbar = loader.get_template('main/navbar.html')
    context['navbar'] = navbar.render(context, request)

    index = loader.get_template('articles/index.html')
    return HttpResponse(index.render(context, request))
