#!/usr/bin/python
# -*- coding: utf-8 -*-

from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS
import gettext
import os
__version__ = "3.2"
PluginLanguageDomain = 'freearhey'
PluginLanguagePath = 'Extensions/freearhey/locale'

isDreamOS = False
if os.path.exists("/var/lib/dpkg/status"):
    isDreamOS = True


def paypal():
    conthelp = "If you like what I do you\n"
    conthelp += "can contribute with a coffee\n"
    conthelp += "scan the qr code and donate € 1.00"
    return conthelp


def localeInit():
    if isDreamOS:
        lang = language.getLanguage()[:2]
        os.environ["LANGUAGE"] = lang
    gettext.bindtextdomain(
        PluginLanguageDomain,
        resolveFilename(
            SCOPE_PLUGINS,
            PluginLanguagePath))


if isDreamOS:
    def _(txt): return gettext.dgettext(
        PluginLanguageDomain, txt) if txt else ""
else:
    def _(txt):
        if gettext.dgettext(PluginLanguageDomain, txt):
            return gettext.dgettext(PluginLanguageDomain, txt)
        else:
            return gettext.gettext(txt)
localeInit()
language.addCallback(localeInit)
