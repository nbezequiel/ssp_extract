#!/usr/bin/env python
# -*- coding: utf-8 -*-


from config.logger_config import Logger
from mongoengine import connect


class DatabaseConfig(Logger):
    
    def __init__(self):
        super().__init__()
        self._conect()
    
    def _conect(self):
        try:
            connect("test")
        except:
            msg = "can't connect to the database"
            self.log.error(msg)
            raise Exception(msg)


