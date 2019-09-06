#!/usr/bin/python3
#
# Listen for tile presses and converts them to http requests.
#
from gpiozero import Button
from time import sleep

import argparse
import requests

parser = argparse.ArgumentParser("Listen for tile presses and converts them to http requests")
parser.add_argument("-k", "--key-server", action="store", dest="keyserver", help="the address of the keyserver", default="http://localhost:9090")
args = parser.parse_args()

buttons = {
    "vagrant": Button(23, pull_up=False),
    "packer": Button(24, pull_up=False),
    "terraform": Button(25, pull_up=False),
    "vault": Button(12, pull_up=False),
    "nomad": Button(16, pull_up=False),
    "consul": Button(20, pull_up=False)
}

WAIT_SLEEP_SECONDS = 0.1

def send_touch(tile):
    url = args.keyserver + "/touch/" + tile
    data = {} 
    r = requests.post(url = url, data = data) 

while True:
    for tile, button in buttons.items():
        if button.is_pressed:
            print("got button press for " + tile)
            send_touch(tile)

    # Wait so we dont block everything else.
    sleep(WAIT_SLEEP_SECONDS)
    
    