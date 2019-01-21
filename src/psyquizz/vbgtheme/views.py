# -*- coding: utf-8 -*-
# # Copyright (c) 2007-2013 NovaReto GmbH
# # cklinger@novareto.de


import uvclight

from .interfaces import IVBGTheme
from nva.psyquizz.browser.frontpages import AccountHomepage


class AccountHomepage(AccountHomepage):
    uvclight.layer(IVBGTheme)
    template = uvclight.get_template('frontpage.pt', __file__)

