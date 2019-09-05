#!/usr/bin/python
#
# Listens for tile presses and converts them to http requests.
#
from gpiozero import Button
import requests
from time import sleep

buttons = {
    "vagrant": Button(23),
    "packer": Button(24),
    "terraform": Button(25),
    "vault": Button(12),
    "nomad": Button(16),
    "consul": Button(20)
}

WAIT_SLEEP_SECONDS = 0.1
KEY_SERVER_ADDRESS = "http://localhost:9090"

def send_touch(self, tile):
    url = KEY_SERVER_ADDRESS + "/touch/" + tile
    data = {} 
    r = requests.post(url = url, data = data) 

while True:
    for tile, button in buttons.iteritems():
        if button.is_pressed:
            print("got button press for " + tile)
            send_touch(tile)

        # Wait so we dont block everything else.
        time.sleep(WAIT_SLEEP_SECONDS)
        
    