
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver import Firefox, FirefoxOptions
from config.webdriver_profile import Profile
from .logger_config import Logger
from utils import SSP_URL


class WebDriver(Firefox, Logger):

    def __init__(self):
        options = FirefoxOptions()
        options.headless = True
        self._driver_path = SSP_URL
        self.executable_path = r"/home/ezequiel/Downloads/geckodriver"
        super(WebDriver, self).__init__(
            executable_path=self.executable_path, options=options)
        self.implicitly_wait(10)
        self._firefox_profile = Profile()
    

    def init(self):
        try:
            self.get(self._driver_path)
        except Exception as ex:
            self.log.error(str(ex))
            raise ex


driver = WebDriver()
