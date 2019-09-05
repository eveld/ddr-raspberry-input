#!/usr/bin/python
#
# Listen for notes and trigger tiles to light up or dim.
# Runs on the pi4.
#
from flask import Flask
from flask_restful import Api, Resource, reqparse

tiles = {
    "all": {
        "enabled": False,
        "start": 0,
        "end": 250,
        "r": 255,
        "g": 255,
        "b": 255
    },
    "vagrant": {
        "enabled": False,
        "start": 0,
        "end": 34,
        "r": 0,
        "g": 84,
        "b": 251
    },
    "packer": {
        "enabled": False,
        "start": 34,
        "end": 68,
        "r": 4,
        "g": 165,
        "b": 255
        },
    "terraform": {
        "enabled": False,
        "start": 68,
        "end": 102,
        "r": 92,
        "g": 78,
        "b": 229
    },
    "vault": {
        "enabled": False,
        "start": 102,
        "end": 136,
        "r": 106,
        "g": 109,
        "b": 122
    },
    "nomad": {
        "enabled": False,
        "start": 136,
        "end": 170,
        "r": 37,
        "g": 186,
        "b": 129
    },
    "consul": {
        "enabled": False,
        "start": 170,
        "end": 204,
        "r": 198,
        "g": 42,
        "b": 113
    },
    "hashicorp": {
        "enabled": False,
        "start": 204,
        "end": 250,
        "r": 255,
        "g": 255,
        "b": 255
    }
}

class Note(Resource):
    def post(self, name):
        tiles[name]["enabled"] = True
        for index in range(tiles[name]["start"], tiles[name]["end"]):
                pixels[index] = (tiles[name]["r"], tiles[name]["g"], tiles[name]["b"])

    def delete(self, name):
        tiles[name]["enabled"] = False
        for index in range(tiles[name]["start"], tiles[name]["end"]):
                pixels[index] = (0, 0, 0)

app = Flask(__name__)
api = Api(app)
api.add_resource(Note, "/note/<string:name>")
app.run(host="0.0.0.0",port=9091,debug=True)