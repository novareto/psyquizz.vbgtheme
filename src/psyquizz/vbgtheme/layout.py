# -*- coding: utf-8 -*-

import uvclight
from zope.interface import Interface
from .interfaces import IVBGTheme
from . import get_template, vbgcss


class Layout(uvclight.Layout):
    uvclight.context(Interface)
    uvclight.layer(IVBGTheme)

    base = "/"
    template = get_template('layout.cpt')

    def __call__(self, content, **ns):
        vbgcss.need()
        site = uvclight.getSite()
        self.title = getattr(site, 'title', 'UVCLight')
        if 'view' in ns:
            if hasattr(ns['view'], 'title'):
                self.title = getattr(ns['view'], 'title', u'UVCLight')
        return uvclight.Layout.__call__(self, content, **ns)
