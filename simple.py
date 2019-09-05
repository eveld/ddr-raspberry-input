#!/usr/bin/python3

from gpiozero import Button
from time import sleep

button = Button(16, pull_up=False)

while True:
    if button.is_pressed:
        print("Pressed")
    else:
        print("Released")
    sleep(1)