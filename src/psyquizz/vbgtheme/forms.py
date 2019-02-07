# -*- coding: utf-8 -*-
# Copyright (c) 2007-2019 NovaReto GmbH
# cklinger@novareto.de

import uvclight

from .interfaces import IVBGTheme
from zope import schema, interface
from nva.psyquizz.models import IAccount
from nva.psyquizz.browser.forms import CreateAccount, CreateCompany
from nva.psyquizz.browser.forms import IVerifyPassword, ICaptched
from nva.psyquizz.models.interfaces import ICompany


class IAckForm(interface.Interface):

    ack_form = schema.Bool(
        title=u"Bestätigung",
        description=u"Hiermit bestätige ich die Datenschutzbestimmungen der \
            VBG gelessen und akzeptiert zu haben. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr",
        required=True,
    )

class CreateAccount(CreateAccount):
    uvclight.layer(IVBGTheme)

    fields = (uvclight.Fields(IAccount).select('name', 'email', 'password') +
        uvclight.Fields(IVerifyPassword, ICaptched)) + uvclight.Fields(IAckForm)


CreateCompany.fields['mnr'].description = u"Bitte geben Sie hier die ersten acht Stellen Ihrer Mitgliedsnummer bei der VBG ein."
