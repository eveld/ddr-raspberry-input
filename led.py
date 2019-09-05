import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 150)#, brightness=1.0, auto_write=False, pixel_order=neopixel.GRB)

pixels.fill((0, 255, 0))