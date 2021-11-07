#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config import Logger, DatabaseConfig
from time import time
from services import Navigator
from factory import elements


class Main(Logger):

    def __init__(self):
        super().__init__()
        self.database = DatabaseConfig()

    def startup(self):
        self.log.debug("---- Starting ----")
        Navigator(elements)

if __name__ == '__main__':
    Main().startup()
