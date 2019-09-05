#!/usr/bin/python
#
# Listen for touch events and forward them to the key-server over HTTP.
# Runs on the pi4.
#
import Adafruit_MPR121.MPR121 as MPR121
import RPi.GPIO as GPIO

import atexit

IRQ_PIN = 26

MAX_EVENT_WAIT_SECONDS = 0.5
EVENT_WAIT_SLEEP_SECONDS = 0.1

KEY_SERVER_ADDRESS = "http://localhost:9090"

pins = {
    0: "vault",
    1: "nomad",
    2: "terraform",
    3: "packer",
    4: "consul",
    5: "vagrant",    
}

cap = MPR121.MPR121()
if not cap.begin():
    print("Failed to initialize MPR121, check the wiring")
    sys.exit(1)

GPIO.setmode(GPIO.BCM)
GPIO.setup(IRQ_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(IRQ_PIN, GPIO.FALLING)
atexit.register(GPIO.cleanup)

# Clear the state
cap.touched()

# Listen for touch events.
while True:
    start = time.time()
    while (time.time() - start) < MAX_EVENT_WAIT_SECONDS and not GPIO.event_detected(IRQ_PIN):
        time.sleep(EVENT_WAIT_SLEEP_SECONDS)
    
    # Read touch state.
    touched = cap.touched()

    for pin, tile in pins.iteritems():
        # Check if pin is touched.
        pin_bit = 1 << pin
        if touched & pin_bit:
            # Send http request to key-server.
            url = KEY_SERVER_ADDRESS + "/touch/" + tile
            data = {} 
            r = requests.post(url = url, data = data) 