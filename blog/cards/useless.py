"""
Loads informations about a repository.
"""

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

from django.template import loader

from . import Card


base_url = 'https://www.savoir-inutile.com'


class UselessCard(Card) :
    template = loader.get_template('cards/useless.html')

    def __init__(self, conf={}) :
        self.context = conf

    def html(self, request) :
        """
        Loads random knowledge.
        """
        req = Request(base_url)
        with urlopen(req) as url :
            parsed = BeautifulSoup(url.read().decode(), 'html.parser')
            self.context['content'] = parsed.find('h2', {'id': 'phrase'}).text
            self.context['url'] = parsed.find('div', {'id': "direct-url"}).find('a')['href']

        return self.template.render(self.context, request)
