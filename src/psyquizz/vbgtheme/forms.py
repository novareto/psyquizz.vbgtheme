# -*- coding: utf-8 -*-
# Copyright (c) 2007-2019 NovaReto GmbH
# cklinger@novareto.de

import uvclight

from .interfaces import IVBGTheme, IVBGRegTheme
from zope import schema, interface
from nva.psyquizz.models import IAccount
from nva.psyquizz.browser.forms import CreateAccount, CreateCompany
from nva.psyquizz.browser.forms import IVerifyPassword, ICaptched
from nva.psyquizz.models.interfaces import ICompany


DESC = u"""
Ja, ich habe die Datenschutzhinweise und die Informationen nach Artikel 13 DSGVO gelesen und stimme diesen zu.
Ich willige ein, dass die VBG meine personenbezogenen Daten im Rahmen des bereitgestellten Online-Verfahrens
zur Gefährdungsbeurteilung psychische Belastung am Arbeitsplatz verarbeitet. Mir ist bekannt, dass ich die
Einwilligung jederzeit widerrufen kann. Durch den Widerruf der Einwilligung wird die Rechtmäßigkeit der
aufgrund der Einwilligung bis zum Widerruf erfolgten Verarbeitung nicht berührt.
"""



class IAckForm(interface.Interface):

    ack_form = schema.Bool(
        title=u"Bestätigung",
        description=DESC,
        required=True,
    )

class CreateAccount(CreateAccount):
    uvclight.layer(IVBGRegTheme)

    fields = (uvclight.Fields(IAccount).select('name', 'email', 'password') +
        uvclight.Fields(IVerifyPassword, ICaptched)) + uvclight.Fields(IAckForm)


class CreateCompany(CreateCompany):
    uvclight.layer(IVBGTheme)
    label = u'Unternehmen anlegen <a href="" data-toggle="modal" data-target="#myModal"> <span class="glyphicon glyphicon-question-sign" aria-hidden="true"></span></a>'

    fields = uvclight.Fields(ICompany).select(
       'name', 'exp_db', 'type', 'employees')
    fields['exp_db'].mode = "blockradio"
