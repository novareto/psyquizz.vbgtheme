# -*- coding: utf-8 -*-
# Copyright (c) 2007-2019 NovaReto GmbH
# cklinger@novareto.de

import uvclight

from .interfaces import IVBGTheme, IVBGRegTheme, IKontaktForm
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

    fields = (uvclight.Fields(IAccount).select('name', 'mnr', 'email', 'password') +
        uvclight.Fields(IVerifyPassword, ICaptched)) + uvclight.Fields(IAckForm)


class CreateCompany(CreateCompany):
    uvclight.layer(IVBGTheme)
    label = u'Unternehmen anlegen <a href="" data-toggle="modal" data-target="#myModal"> <span class="glyphicon glyphicon-question-sign" aria-hidden="true"></span></a>'

    fields = uvclight.Fields(ICompany).select(
       'name', 'exp_db', 'type', 'employees')
    fields['exp_db'].mode = "blockradio"



class KontaktForm(uvclight.Form):
    uvclight.name('kontakt')
    uvclight.context(interface.Interface)
    uvclight.layer(IVBGTheme)
    uvclight.auth.require('zope.Public')

    fields = uvclight.Fields(IKontaktForm)

    label = u"Kontakt"
    description = u"Hier haben Sie die Möglichkeit uns themenspezifische Nachrichten zukommen zu lassen"

    @uvclight.action('Abbrechen')
    def handle_save(self):
        self.redirect(self.application_url())

    @uvclight.action('Senden')
    def handle_save(self):
        data, errors = self.extractData()
        if errors:
            self.flash('Es sind Fehler aufgetreten')
            return 
        from nva.psyquizz.emailer import ENCODING
        config = self.context.configuration
        subject_choices = self.fields['subject'].getChoices(self)
        item = subject_choices.getTerm(data['subject'])
        subject = item.title
        email, suf = item.token.split('_')

        tpl = config.resources.get_template('contact.tpl')
        emailer = self.context.configuration.emailer
        # {'message': u'fsadff', 'email': u'ck@novareto.de', 'subject': '1'}
        title = "Anfrage!".encode(ENCODING)
        #email = data['email']
        data['encoding'] = ENCODING
        data['subject'] = subject
        with config.emailer as sender:
            mail = config.emailer.prepare_from_template(tpl, email, title, data)
            sender(email, mail.as_string())
        self.flash('Ihre Anfrage wurde versendet.')
        self.redirect(self.application_url())

