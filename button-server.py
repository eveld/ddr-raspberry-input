#!/usr/bin/python3
#
# Listens for tile presses and converts them to http requests.
#
from gpiozero import Button
import requests
from time import sleep

buttons = {
    "vagrant": Button(23, pull_up=False),
    "packer": Button(24, pull_up=False),
    "terraform": Button(25, pull_up=False),
    "vault": Button(12, pull_up=False),
    "nomad": Button(16, pull_up=False),
    "consul": Button(20, pull_up=False)
}

WAIT_SLEEP_SECONDS = 0.1
KEY_SERVER_ADDRESS = "http://localhost:9090"

def send_touch(tile):
    url = KEY_SERVER_ADDRESS + "/touch/" + tile
    data = {} 
    r = requests.post(url = url, data = data) 

while True:

    for tile, button in buttons.items():
        if button.is_pressed:
            print("got button press for " + tile)
            send_touch(tile)

    # Wait so we dont block everything else.
    sleep(WAIT_SLEEP_SECONDS)
    
    