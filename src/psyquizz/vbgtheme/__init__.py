# -*- coding: utf-8 -*-

import logging
import uvclight
#from os import path
from fanstatic import Library, Resource  #, Group
from grokcore.component import context, Subscription
from nva.psyquizz.models.interfaces import IQuizzSecurity
from zope.interface import implementer, Interface


library = Library('psyquizz.vbgtheme', 'static')
vbgcss = Resource(library, 'vbg.css')
vbgjs = Resource(library, 'vbg.js')


def get_template(name):
    return uvclight.get_template(name, __file__)


@implementer(IQuizzSecurity)
class SecurityCheck(Subscription):
    context(Interface)

    def check(self, name, quizz, context):
        if name == 'quizz3' or name == 'quizz2':
            return False
        return True
