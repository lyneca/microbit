from microbit import *
import neopixel

COLOR = (255, 255, 255)

strip = neopixel.NeoPixel(pin0, 30)

def dim(color, brightness):
    return tuple(int(c * ((brightness / 10))) for c in color)

def show_symbol(s):
    '''Send a symbol to the neopixel strip, skipping every 5th LED (offset by one)'''
    strip.clear()
    for y, row in enumerate(s.split(':')):
        for x, pixel in enumerate(row):
            strip[y * 6 + x % 5] = dim(COLOR, int(pixel))
    strip.show()

def animate_symbol(array, delay=100):
    for symbol in array:
        show_symbol(symbol)
        sleep(delay)

s = ('10001:'
     '10001:'
     '10001:'
     '10001:'
     '11111:')

show_symbol(s)
