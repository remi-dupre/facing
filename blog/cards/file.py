# -*- coding: utf-8 -*-
"""
Loads informations about a repository.
"""

from django.template import loader

from . import Card


class FileCard(Card) :
    template = loader.get_template('cards/file.html')

    def __init__(self, conf) :
        """
        conf must contain :
         - name
         - description
         - path
         - date
        Optional :
         - filetype
         - subtitle
        """
        self.context = conf

        if 'filetype' not in self.context.keys() :
            self.context['filetype'] = conf['path'].split('.')[-1]

        if 'subtitle' not in self.context.keys() :
            self.context['subtitle'] = 'Télécharger ' + conf['path']
