#!/usr/bin/python3
#
# Listen for notes and trigger tiles to light up or dim.
# Runs on the pi4.
#
from flask import Flask
from flask_restful import Api, Resource, reqparse

import argparse
import board
import neopixel

parser = argparse.ArgumentParser("Listen for notes and trigger tiles to light up or dim")
parser.add_argument("-l", "--listen", action="store", dest="listen", help="the address to listen on", default="localhost")
parser.add_argument("-p", "--port", action="store", dest="port", help="port", default=9090)
args = parser.parse_args()

pixels = neopixel.NeoPixel(board.D18, 250, brightness=1.0, auto_write=False, pixel_order=neopixel.GRB)

tiles = {
    "teal": {
        "enabled": False,
        "start": 0,
        "end": 250,
        "r": 0,
        "g": 255,
        "b": 255
    },
    "yellow": {
        "enabled": False,
        "start": 0,
        "end": 250,
        "r": 255,
        "g": 255,
        "b": 0
    },
    "purple": {
        "enabled": False,
        "start": 0,
        "end": 250,
        "r": 255,
        "g": 0,
        "b": 255
    },
    "white": {
        "enabled": False,
        "start": 0,
        "end": 250,
        "r": 255,
        "g": 255,
        "b": 255
    },
    "blue": {
        "enabled": False,
        "start": 0,
        "end": 250,
        "r": 0,
        "g": 0,
        "b": 255
    },
    "green": {
        "enabled": False,
        "start": 0,
        "end": 250,
        "r": 0,
        "g": 255,
        "b": 0
    },
    "red": {
        "enabled": False,
        "start": 0,
        "end": 250,
        "r": 255,
        "g": 0,
        "b": 0
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
        if name in tiles:
            tile = tiles[name]
            for index in range(tile["start"], tile["end"]):
                pixels[index] = (tiles[name]["r"], tiles[name]["g"], tiles[name]["b"])
            pixels.show()
            return "turned on " + name
        else:
            return "unknown led"

    def delete(self, name):
        if name in tiles:
            tile = tiles[name]
            for index in range(tile["start"], tile["end"]):
                pixels[index] = (0, 0, 0)
            pixels.show()
            return "turned off " + name
        else:
            return "unknown led"

app = Flask(__name__)
api = Api(app)
api.add_resource(Note, "/note/<string:name>")
app.run(host=args.listen,port=args.port,debug=True)