import uvclight
import itertools
from zope import interface
from zope import schema
from . import get_template
from .interfaces import IVBGTheme
from dolmen.forms.base.actions import Action, Actions
from nva.psyquizz.interfaces import ICompanyRequest
from nva.psyquizz.browser.invitations import DownloadLetter
from nva.psyquizz.browser.lib.emailer import SecureMailer, prepare, ENCODING
from dolmen.forms.base import FAILURE


class Datenschutz(uvclight.Page):
    uvclight.context(interface.Interface)
    uvclight.layer(ICompanyRequest)
    uvclight.auth.require('zope.Public')

    template = get_template('datenschutz.cpt')


class IEmailer(interface.Interface):
    emails = schema.Text(title=u"Recipients", required=False)


class EmailAction(Action):

    def tokens(self, form):
        url = form.application_url() + '/befragung'
        for a in itertools.chain(
                form.context.complete, form.context.uncomplete):
            yield url, str(a.access)

    @staticmethod
    def send(smtp, text, tokens, *recipients):
        mailer = SecureMailer(smtp, port=8025)  # BBB 
        from_ = 'extranet@bgetem.de'
        title = (u'FIX ME').encode(ENCODING)

        with mailer as sender:
            for email in recipients:
                url, token = next(tokens)
                body = "%s\r\n\r\nDie Internetadresse lautet: <b> %s/befragung</b> <br/> Ihr Kennwort lautet: <b> %s</b>" % (text.encode('utf-8'), url, token)
                mail = prepare(from_, email, title, body, body)
                sender(from_, email, mail.as_string())

    def __call__(self, form):
        data, errors = form.extractData()
        if errors:
            form.flash(u"Es ist ein Fehler aufgetreten")
            return FAILURE
        tokens = self.tokens(form)
        recipients = (e.strip() for e in data['emails'].split('\n'))
        smtp = uvclight.getSite().configuration.smtp_server
        sent = self.send(smtp, data['text'], tokens, *recipients)
        response = form.responseFactory()
        response.redirect(form.url(form.context), status=302)
        return response


class LetterEmailer(DownloadLetter):
    uvclight.name('downloadletter')
    uvclight.layer(IVBGTheme)

    fields = DownloadLetter.fields + uvclight.Fields(IEmailer)
    actions = DownloadLetter.actions + Actions(EmailAction('Send by mail'))


