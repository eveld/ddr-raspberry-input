import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 250, brightness=1.0, auto_write=False, pixel_order=neopixel.GRB)

pixels.fill()