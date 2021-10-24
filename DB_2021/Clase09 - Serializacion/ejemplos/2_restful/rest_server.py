#!/usr/bin/env python
from flask import Flask, jsonify
from flask_restful import Resource, Api
import model

app = Flask(__name__)
api = Api(app)


@api.resource('/artists/')
class ArtistsList(Resource):
    def get(self):
        return jsonify(model.listAll())
        # return jsonify(model.finder("Itzhak Perlman".replace('|', '/')))

if __name__ == '__main__':
    app.run(debug=True, port=4000)
