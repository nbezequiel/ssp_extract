#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver import FirefoxProfile


class Profile(FirefoxProfile):
    def __init__(self):
        super(Profile, self).__init__()
        self._set_preferences()

    def _set_preferences(self):
        self.set_preference("browser.download.folderList", 2)
        self.set_preference("browser.download.manager.showWhenStarting", False)
        self.set_preference("browser.download.dir", "/home/ezequiel/tcc/")
        self.set_preference(
            "browser.helperApps.neverAsk.saveToDisk", "application/text"
        )
        self.accept_untrusted_certs = True

