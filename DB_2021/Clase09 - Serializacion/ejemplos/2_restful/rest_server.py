#!/usr/bin/env python
from flask import Flask, jsonify
from flask_restful import Resource, Api
import model

app = Flask(__name__)
api = Api(app)


@api.resource('/artists2/')
class ArtistsList(Resource):
    def get(self):
        print(model.Artist.select())
        return jsonify([a.name for a in model.Artist.select()])


@api.resource('/artists/')
class ArtistAndAlbums(Resource):
    def get(self):
        return jsonify(model.finder("Nash Ensemble".replace('|', '/')))


if __name__ == '__main__':
    app.run(debug=True)
