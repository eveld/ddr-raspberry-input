Install dependencies.
```
sudo pip install python-uinput gpiozero flask flask_restful rpi_ws281x adafruit-circuitpython-neopixel
```

Run in separate windows.
Key server waits for messages and then triggers a key-press.
```
sudo python key-server.py
```

Led server waits for messages and then turns leds on or off.
```
sudo led-server.py
```

Button server waits for gpio input and then sends a message to the key-server.
```
sudo button-server.py
```