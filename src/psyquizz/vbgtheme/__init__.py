# -*- coding: utf-8 -*-

import logging
import uvclight
#from os import path
from fanstatic import Library, Resource  #, Group


library = Library('psyquizz.vbgtheme', 'static')
vbgcss = Resource(library, 'vbg.css')
vbgjs = Resource(library, 'vbg.js')


def get_template(name):
    return uvclight.get_template(name, __file__)
