# -*- coding: utf-8 -*-
# Copyright (c) 2007-2021 NovaReto GmbH
# cklinger@novareto.de


import uvclight


from .interfaces import IVBGTheme
from reportlab.lib.units import cm
from nva.psyquizz.browser.pdf import GeneratePDF
from nva.psyquizz.browser.pdf.quizz1 import PDFPL
from nva.psyquizz.browser.pdf.quizz3 import PDF_WAI
from nva.psyquizz.browser.pdf.quizz5 import Quizz5PDF


class Quizz5PDF(Quizz5PDF):
    uvclight.layer(IVBGTheme)

    def headerfooter(self, canvas, doc):
        canvas.setFont("Helvetica", 9)
        canvas.drawString(1 * cm, 2 * cm, u"Gut gestaltete Arbeitsbedingungen")
        canvas.drawString(1 * cm, 1.6 * cm, u"Psychische Belastungen online erfassen")
        canvas.drawString(1 * cm, 1.2 * cm, u"Ein Programm der VBG")
        canvas.drawString(15 * cm, 2 * cm, u"Grundlage der Befragung:")
        canvas.drawString(15 * cm, 1.6 * cm, u"FBGU-Fragebogen")
        canvas.setFont("Helvetica", 12)


class GeneratePDF(GeneratePDF):
    uvclight.layer(IVBGTheme)

    def headerfooter(self, canvas, doc):
        canvas.setFont("Helvetica", 9)
        canvas.drawString(1 * cm, 2 * cm, u"Gemeinsam zu gesunden Arbeitsbedingungen")
        canvas.drawString(1 * cm, 1.6 * cm, u"Psychische Belastungen online erfassen")
        canvas.drawString(1 * cm, 1.2 * cm, u"Ein Programm der VBG")
        canvas.drawString(18 * cm, 2 * cm, u"Grundlage der Befragung: KFZA - Kurzfragebogen")
        canvas.drawString(18 * cm, 1.6 *cm, u"zur Arbeitsanalyse")
        canvas.drawString(18 * cm, 1.2 * cm, u"Prümper, J., Hartmannsgruber, K. & Frese, M")
        canvas.line(0.5 * cm , 2.5 * cm, 26 * cm, 2.5 * cm)
        canvas.setFont("Helvetica", 12)



class PDFPL(PDFPL):
    uvclight.layer(IVBGTheme)

    def headerfooter(self, canvas, doc):
        canvas.setFont("Helvetica", 9)
        canvas.drawString( 1 * cm, 2 * cm, u"Gemeinsam zu gesunden Arbeitsbedingungen")
        canvas.drawString( 1 * cm, 1.6 * cm, u"Psychische Belastungen online erfassen")
        canvas.drawString( 1 * cm, 1.2 * cm, u"Ein Programm der VBG")
        canvas.drawString( 18 * cm, 2 * cm, u"Grundlage der Befragung:  Prüfliste Psychische")
        canvas.drawString( 18 * cm, 1.6 *cm, u"Belastung")
        canvas.drawString( 18 * cm, 1.2 * cm, u"Unfallversicherung Bund und Bahn")
        canvas.line(0.5 * cm , 2.5 * cm, 26 * cm, 2.5 * cm)


class PDF_WAI(PDF_WAI):
    uvclight.layer(IVBGTheme)

    def headerfooter(self, canvas, doc):
        action = self.request.form.get('action')
        canvas.setFont("Helvetica", 9)
        canvas.drawString(1 * cm, 2 * cm, u"Gemeinsam zu gesunden Arbeitsbedingungen")
        canvas.drawString(1 * cm, 1.6 * cm, u"Psychische Belastungen online erfassen")
        canvas.drawString(1 * cm, 1.2 * cm, u"Ein Programm der VBG")
        if doc.page >= 3 or action == "wai":
            canvas.drawString(18 * cm, 2 * cm, u"Grundlage der Befragung")
            canvas.drawString(18 * cm, 1.6 *cm, u"Work Ability Index (WAI)")
            canvas.drawString(18 * cm, 1.2 * cm, u"Ilmarinen, Tuomi")

        else:
            canvas.drawString(18 * cm, 2 * cm, u"Grundlage der Befragung: KFZA - Kurzfragebogen")
            canvas.drawString(18 * cm, 1.6 *cm, u"zur Arbeitsanalyse")
            canvas.drawString(18 * cm, 1.2 * cm, u"Prümper, J., Hartmannsgruber, K. & Frese, M")
        canvas.line(0.5 * cm, 2.5 * cm, 26 * cm, 2.5 * cm)
        canvas.setFont("Helvetica", 12)
