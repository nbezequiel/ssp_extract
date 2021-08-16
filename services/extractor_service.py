#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver.firefox.webelement import FirefoxWebElement
from model import Occurrence
from mapper import OccurrenceMapper
from config import Logger

class Extractor(Logger):

    MAX_COLUMNS = 14

    def __init__(self):
        super().__init__()
        self._months = []
        self._count = 0

    def extract(self, year, department, elements):
        ocurrencies = self._get_occurrences(year, department, elements)
        try:
            self._set_data(year, department, ocurrencies)
        except Exception as e:
            self.log.error("Erro when trying to set_data: %s", e)

    def _get_occurrences(self, year, department, elements):
        all_occurrences = []

        for element in elements:
            self._count_increment()
            self._months.append(element.text)

            if self._count == self.MAX_COLUMNS:
                all_occurrences.append(self._months)
                self._reset_months()

        self.log.info("all lines to %s" % department)
        return all_occurrences

    def _reset_months(self):
        self._count = 0
        self._months = []

    def _count_increment(self):
        self._count += 1

    def _set_data(self, year, department, ocurrencies):
        occurrences_to_save = []
        for values in ocurrencies:
            occurrencie = OccurrenceMapper.values_to_occurrence(values, year, department)
            occurrences_to_save.append(occurrencie)
        if len(occurrences_to_save) > 0:
            Occurrence.objects.insert(occurrences_to_save)
    
