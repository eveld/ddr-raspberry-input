Install dependencies.
```
sudo pip3 install python-uinput gpiozero flask flask_restful rpi_ws281x adafruit-circuitpython-neopixel Adafruit-Blinka
```

Run in separate windows.
Key server waits for messages and then triggers a key-press.
```
sudo python3 key-server.py
```

Led server waits for messages and then turns leds on or off.
```
sudo python3 led-server.py
```

Button server waits for gpio input and then sends a message to the key-server.
```
sudo python3 button-server.py
```