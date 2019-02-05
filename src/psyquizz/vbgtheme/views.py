# -*- coding: utf-8 -*-
# # Copyright (c) 2007-2013 NovaReto GmbH
# # cklinger@novareto.de


import uvclight
from zope import interface
from . import get_template
from nva.psyquizz.interfaces import ICompanyRequest


class Datenschutz(uvclight.Page):
    uvclight.context(interface.Interface)
    uvclight.layer(ICompanyRequest)
    uvclight.auth.require('zope.Public')

    template = get_template('datenschutz.cpt')

