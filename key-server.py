#!/usr/bin/python3
#
# Listen for touch events and trigger a key-press on the host.
# Runs on the laptop.
#
from flask import Flask
from flask_restful import Api, Resource, reqparse

import subprocess
import uinput

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
        print("received touch for " + name)
        device.emit_click(keys[name])
        return "ok", 200

app = Flask(__name__)
api = Api(app)
api.add_resource(Touch, "/touch/<string:name>")
app.run(host="0.0.0.0",port=9090,debug=True)