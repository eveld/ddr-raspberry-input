#!/usr/bin/python3

from gpiozero import Button
from time import sleep

button = Button(16, pull_up=True)
button.wait_for_press()
print("The button was pressed!")