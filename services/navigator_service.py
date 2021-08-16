#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver.support.select import Select
from config import Logger, driver
from .extractor_service import Extractor
from .filter_service import Filter


class Navigator(Logger):

    def __init__(self, node=None):
        super().__init__()
        self._driver =  driver
        self._extractor = Extractor()
        self._filter = Filter()
        self._saved = []
        self._run(node)
        
    def _run(self, node):
        if self._filter.is_finished():
            return self._driver.close() 
        try:
            self._driver.init()
            node.execute_action()
            self._driver.close()
        except Exception as ex:
            self.log.error(ex)
            ## run until finished
            self._run(node)