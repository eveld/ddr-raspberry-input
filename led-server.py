#!/usr/bin/python3
#
# Listen for notes and trigger tiles to light up or dim.
# Runs on the pi4.
#
from flask import Flask
from flask_restful import Api, Resource, reqparse
import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 250, brightness=1.0, auto_write=False, pixel_order=neopixel.GRB)

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
        tile = tiles[name]
        for index in range(tile["start"], tile["end"]):
            pixels[index] = (tiles[name]["r"], tiles[name]["g"], tiles[name]["b"])
            print(str(index) + " = " + str((tiles[name]["r"], tiles[name]["g"], tiles[name]["b"])))
        pixels.show()
        return "turned on " + name

    def delete(self, name):
        tile = tiles[name]
        for index in range(tile["start"], tile["end"]):
            pixels[index] = (0, 0, 0)
            print(str(index) + " = " + str((0, 0, 0)))
        pixels.show()
        return "turned off " + name

app = Flask(__name__)
api = Api(app)
api.add_resource(Note, "/note/<string:name>")
app.run(host="0.0.0.0",port=9091,debug=True)