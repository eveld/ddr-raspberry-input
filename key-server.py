#!/usr/bin/python3
#
# Listen for touch events and trigger a key-press on the host.
# Runs on the laptop.
#
from flask import Flask
from flask_restful import Api, Resource, reqparse

import argparse
import subprocess
import uinput

parser = argparse.ArgumentParser("Listen for touch events and trigger a key-press on the host")
parser.add_argument("-l", "--listen", action="store", dest="listen", help="the address to listen on", default="localhost")
parser.add_argument("-p", "--port", action="store", dest="port", help="port", default=9090)
args = parser.parse_args()

keys = {
    "vagrant": uinput.KEY_S,
    "packer": uinput.KEY_D,
    "terraform": uinput.KEY_E,
    "vault": uinput.KEY_Q,
    "nomad": uinput.KEY_Q,
    "consul": uinput.KEY_W
}

subprocess.check_call(['modprobe', 'uinput'])
device = uinput.Device(keys.values())

class Touch(Resource):
    def post(self, name):
        if name in keys:
            device.emit_click(keys[name])
            return "ok", 200
        else:
            return "unknown key", 404

app = Flask(__name__)
api = Api(app)
api.add_resource(Touch, "/touch/<string:name>")
app.run(host=args.listen,port=args.port,debug=True)