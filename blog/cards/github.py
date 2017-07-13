# -*- coding: utf-8 -*-
"""
Loads informations about a repository.
"""

import json
from datetime import datetime
from urllib.request import urlopen, Request

from django.template import loader

from . import Card


base_api_url = 'https://api.github.com'
api_token = '50db7f5c6dee098b8fe46be305490282abec0294'  # grogrogrogro


class GithubCard(Card) :
    template = loader.get_template('cards/github.html')

    def __init__(self, conf) :
        # load repo informations
        req = Request('%s/repos/%s' % (base_api_url, conf['repo']))
        req.add_header('Authorization', 'token ' + api_token)
        with urlopen(req) as url :
            repo = json.loads(url.read().decode())

        # load owner informations
        req = Request(repo['owner']['url'])
        req.add_header('Authorization', 'token ' + api_token)
        with urlopen(req) as url :
            owner = json.loads(url.read().decode())

        self.context = {
            'name': repo['name'],
            'repository': conf['repo'],
            'description': repo['description'],
            'owner': owner['name'] if owner['name'] is not None else owner['login'],

            'url': repo['html_url'],
            'download': repo['html_url'] + '/archive/master.zip',

            'last_modified': datetime.strptime(repo['updated_at'], '%Y-%m-%dT%H:%M:%SZ').strftime('%d/%m/%Y'),
            'language': repo['language'],

            'release_btn': 'release_btn' in conf.keys() and conf['release_btn'],
            'download_btn': 'download_btn' in conf.keys() and conf['download_btn']
        }

        # load releases informations
        if self.context['release_btn'] :
            req = Request(repo['releases_url'].replace('{/id}', ''))
            req.add_header('Authorization', 'token ' + api_token)
            with urlopen(req) as url :
                releases = json.loads(url.read().decode())
                releases.sort(key=lambda x : x['created_at'])
            self.context['last_release'] = {
                'tag': releases[-1]['tag_name'],
                'url': releases[-1]['html_url']
            }
