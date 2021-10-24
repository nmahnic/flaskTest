#!/usr/bin/env python
import sqlobject as so
import os
import defs

# uri = "mysql://{}:{}@{}/{}".format(defs.USER,defs.PASSWORD,defs.HOST,defs.DBASE)
# print(uri)
# connection = so.connectionForURI(uri)
connection = so.connectionForURI("mysql://guest:guest@localhost/Enerfi")
so.sqlhub.processConnection = connection


class User(so.SQLObject):
    name = so.StringCol(length=50, varchar=True)
    surname = so.StringCol(length=50, varchar=True)
    surname = so.StringCol(length=50, varchar=True)
    userName = so.StringCol(length=50, varchar=True)
    passwd = so.StringCol(length=50, varchar=True)
    mail = so.StringCol(length=50, varchar=True)


def to_dict(obj):
    d = dict((c, getattr(obj, c)) for c in obj.sqlmeta.columns)
    d['id'] = obj.id
    return d


def finder(name):
    artist = User.selectBy(name=name).getOne()
    d = to_dict(artist)
    return d
