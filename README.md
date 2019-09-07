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

```
   laptop                                      raspberry pi

 key-server |   <--- -XPOST /touch/nomad --- | button-server | <--- press nomad --- [ trigger ]
   :9090    |                                |               |
      |     |                                |               |      
      |     |                                |               |
     "q"    |                                |               |
      |     |                                |               |
      v     |                                |               |
     game   |   ---- -XPOST /note/nomad ---> |  led-server   | --- turn nomad on ---> [ leds ]
            |                                |    :9090      |
```

# Pins
Trigger data on GPIO 23,24,25,12,16,20 (see raspberry pi bottom for colors) yellow,black,green - green,red,blue
Trigger ground on GPIO6

Led data on GPIO18
Led ground on G14

