# -*- coding: utf-8 -*-
"""
Keeps informations and renders template for a card.
"""


class Card :
    """
    Generic class for a card.
    """

    template = None  # a base template for this kind of card

    def __init__(self, conf) :
        """
        Loads informations needed to generate the card.
        Must define self.context
        """
        raise Exception('Virtual method')

    def html(self, request) :
        """
        Return html of the card.
        """
        return self.template.render(self.context, request)
