#!/usr/bin/env python
from flask import Flask, jsonify
from flask_restful import Resource, Api
import model

app = Flask(__name__)
api = Api(app)

@api.resource('/user/')
class userList(Resource):
    def get(self):
        print(model.User.select())
        # for a in model.User.select():
            # print(a)
        print(model.finder("Nicolas"))
        return jsonify()
        # return jsonify([a.name for a in model.User.select()])

if __name__ == '__main__':
    app.run(debug=True)
