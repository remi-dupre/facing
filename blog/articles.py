# -*- coding: utf-8 -*-
"""
Gestion of generic articles written in markdown.
"""

import os, sys
import yaml
import markdown2

import django.utils.autoreload

from .cards.github import GithubCard
from .cards.file import FileCard


# Loads informations about articles from index.yaml
root_dir = os.path.dirname(__file__) + '/../articles'
desc_file = root_dir + '/index.yaml'

# Reloads when modification are oppered on root dir
django.utils.autoreload._cached_filenames.append(root_dir)

# load general description
with open(desc_file, 'r', encoding='utf-8') as f:
    descs = yaml.load(f)


# Loads main content
print('Opening articles descriptions')
for art_key in descs :
    try:
        filename = root_dir + '/' + descs[art_key]['content']
        django.utils.autoreload._cached_filenames.append(filename)
        with open(filename, 'r', encoding='utf-8') as f :
            descs[art_key]['content'] = f.read()
            descs[art_key]['html'] = markdown2.markdown(
                descs[art_key]['content'],
                extras=["fenced-code-blocks", "code-color", "footnotes"]
            )
    except Exception as exc:
        print('An error occured while reading %s\'s content : %s' % (art_key, str(exc)))


# Loads cards
print('Loading articles attachments')
for art_key in descs :
    cards_conf = descs[art_key]['attachments']
    descs[art_key]['cards'] = []

    nb_attached = len(cards_conf)
    for i in range(nb_attached) :
        print('%s (%d/%d) [%s]' % (art_key, i+1, nb_attached, cards_conf[i]['type']), end='\r')

        if cards_conf[i]['type'] == 'github' :
            descs[art_key]['cards'].append(GithubCard(cards_conf[i]))
        if cards_conf[i]['type'] == 'file' :
            descs[art_key]['cards'].append(FileCard(cards_conf[i]))
