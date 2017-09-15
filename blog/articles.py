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
root_dir = os.path.realpath(os.path.dirname(__file__) + '/../articles')
desc_file = root_dir + '/index.yaml'

# Reloads when modification are oppered on root dir
django.utils.autoreload._cached_filenames.append(root_dir)


descs = {}


# Loads main content
print('Opening articles descriptions')
for cat in os.listdir(root_dir) :  # open each category directories
    if os.path.isdir(root_dir + '/' + cat) :
        # Load categories indexes
        filename = os.path.join(root_dir, cat, 'index.yaml')
        print('-> Loading articles in ' + filename)
        with open(filename, 'r', encoding='utf-8') as f :
            descs.update({cat: yaml.load(f)})

        # Load articles content
        for art, art_description in descs[cat]['articles'].items() :  # open each article
            filename = os.path.join(root_dir, art_description['content'])
            print(' - Loading content from ' + filename)
            with open(filename, 'r', encoding='utf-8') as f :
                art_description['content'] = f.read()
                art_description['html'] = markdown2.markdown(
                    art_description['content'],
                    extras=["fenced-code-blocks", "code-color", "footnotes", "header-ids"]
                )

            # Load article's cards
            art_description['cards'] = []  # where cards code will vbe loaded
            cards_conf = art_description['attachments']
            nb_attachments = len(cards_conf)
            for i in range(nb_attachments) :
                print('    card for %s (%d/%d) [%s]' % (art, i+1, nb_attachments, cards_conf[i]['type']))

                if cards_conf[i]['type'] == 'github' :
                    art_description['cards'].append(GithubCard(cards_conf[i]))
                if cards_conf[i]['type'] == 'file' :
                    art_description['cards'].append(FileCard(cards_conf[i]))
