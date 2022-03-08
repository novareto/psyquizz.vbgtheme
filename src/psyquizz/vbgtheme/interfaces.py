# -*- coding: utf-8 -*-

from grokcore.component import provider
from zope.interface import Interface
from zope import schema
from uvc.themes.btwidgets import IBootstrapRequest
from nva.psyquizz.models import deferred_vocabularies
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary
from nva.psyquizz.models.interfaces import IAccount


class IVBGTheme(IBootstrapRequest):
     pass


class IVBGRegTheme(IBootstrapRequest):
     pass


@provider(IContextSourceBinder)
def vocab_type(context):
    rc = [SimpleTerm('1', '1', u'Zeitarbeit'),
        SimpleTerm('2', '2', u'Bildungseinrichtungen'),
        SimpleTerm('3', '3', u'Bühnen und Studios'),
        SimpleTerm('4', '4', u'Keramische und Glas-Industrie'),
        SimpleTerm('5', '5', u'Kirchen'),
        SimpleTerm('6', '6', u'Kreditinstitute und Spielstätten'),
        SimpleTerm('7', '7', u'ÖPNV/Bahnen'),
        SimpleTerm('8', '8', u'Sicherungsdienstleistungen'),
        SimpleTerm('9', '9', u'Sport'),
        SimpleTerm('15', '15', u'sonstige'),
    ]
    return SimpleVocabulary(rc)


@provider(IContextSourceBinder)
def vocab_employees(context):
    rc = [SimpleTerm('1', '1', u'Weniger als 10'),
        SimpleTerm('2', '2', u'10-49'),
        SimpleTerm('3', '3', u'50-249'),
        SimpleTerm('4', '4', u'250-499'),
        SimpleTerm('5', '5', u'Größer 500')
    ]
    return SimpleVocabulary(rc)


deferred_vocabularies['type'] = vocab_type
deferred_vocabularies['employees'] = vocab_employees


@provider(IContextSourceBinder)
def kontakt_reason(context):
    rc = [SimpleTerm('1', 'Ulf.Krummreich@vbg.de_1', u'Fehler beim Anmelden'),
#        SimpleTerm('2', 'ck@novareto.de_2', u'Frage zum Zebra-Fragebogen'),
        SimpleTerm('3', 'Ulf.Krummreich@vbg.de_3', u'Frage zum FBGU-Fragebogen'),
    ]
    return SimpleVocabulary(rc)


class IKontaktForm(Interface):

    subject = schema.Choice(
        title=u"Betreff",
        description=u"Bitten wählen Sie aus um was es sich bei Ihrem Anliegen handelt",
        source=kontakt_reason,
        required=True
    )

    email = schema.TextLine(
        title=u"E-Mail",
        description=u"Bitten teilen Sie uns noch Ihre E-Mail Adresse für Rückfragen mit.",
        required=True
    )

    message = schema.Text(
        title=u"Nachricht",
        description=u"",
        required=True
    )
