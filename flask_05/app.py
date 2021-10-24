#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request
import MySQLdb
import json
import defs

app = Flask(__name__)
conn = MySQLdb.connect(host=defs.HOST,
                        user=defs.USER,
                        passwd=defs.PASSWORD,
                        db=defs.DBASE)


def listar_usuarios():
    cur = conn.cursor()
    cur.execute("SELECT * FROM User ORDER BY UserID ASC")
    res = cur.fetchall()
    print(res)
    cur.close()
    conn.close()
    return res


def listar_meter(user):
    print(user)
    cur = conn.cursor()
    query = "SELECT * FROM User JOIN Meter ON (User.UserID = Meter.UserID) WHERE User.UserName={} ORDER BY User.Surname ASC".format(user.upper())
    cur.execute(query)
    res = cur.fetchall()
    print(res)
    cur.close()
    conn.close()
    return res


@app.route("/")
def ping():
    return "pong!"


@app.route("/users", methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        data = request.json
        print(data)
        return json.dumps(data)
    else:
        lista = listar_usuarios()
        return json.dumps(lista)


@app.route("/meter/<usuario>")
def meterByUser(usuario):
    meter = listar_meter(usuario)
    return json.dumps(meter)


if __name__ == '__main__':
    app.debug = True
    app.run()
