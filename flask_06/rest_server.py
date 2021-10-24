#!/usr/bin/env python
from flask import Flask, jsonify
from flask_restful import Resource, Api
import model

app = Flask(__name__)
api = Api(app)

@api.resource('/user/')
class userList(Resource):
    def get(self):
        a = model.listAlluser()
        # print(a)
        return jsonify(a)

@api.resource('/dum/')
class dumList(Resource):
    def get(self):
        a = model.listAlldum()
        # print(a)
        return jsonify(a)

if __name__ == '__main__':
    app.run(debug=True)
