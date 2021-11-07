#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mongoengine import Document, StringField


class Occurrence(Document):

    department = StringField()

    year = StringField()

    occurrence = StringField()

    jan = StringField()

    feb = StringField()

    mar = StringField()

    apr = StringField()

    may = StringField()

    jun = StringField()

    jul = StringField()

    aug = StringField()

    sep = StringField()

    oct = StringField()

    nov = StringField()

    dec = StringField()

    total = StringField()
