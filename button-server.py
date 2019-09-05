#!/usr/bin/python3
#
# Listens for tile presses and converts them to http requests.
#
from gpiozero import Button
import requests
from time import sleep

buttons = {
    "vagrant": Button(16),
    "packer": Button(18),
    "terraform": Button(22),
    "vault": Button(32),
    "nomad": Button(36),
    "consul": Button(38)
}

WAIT_SLEEP_SECONDS = 0.1
KEY_SERVER_ADDRESS = "http://localhost:9090"

def send_touch(self, tile):
    url = KEY_SERVER_ADDRESS + "/touch/" + tile
    data = {} 
    r = requests.post(url = url, data = data) 

while True:

    # for tile, button in buttons.iteritems():
    if buttons["vagrant"].is_pressed:
        print("got button press for vagrant")
    if buttons["nomad"].is_pressed:
        print("got button press for nomad")
    if buttons["consul"].is_pressed:
        print("got button press for consul")
    if buttons["vault"].is_pressed:
        print("got button press for vault")
    if buttons["terraform"].is_pressed:
        print("got button press for terraform")
    if buttons["packer"].is_pressed:
        print("got button press for packer")
        # send_touch(tile)

    # Wait so we dont block everything else.
    time.sleep(WAIT_SLEEP_SECONDS)
    
    