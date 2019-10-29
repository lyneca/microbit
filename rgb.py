from microbit import *
import utime

# Usage:
# set_color(255, 0, 0)

def clk():
    pin0.write_digital(0)
    utime.sleep_us(20)
    pin0.write_digital(1)
    utime.sleep_us(20)

def send_byte(b):
    for i in range(8):
        if (b & 0x80) != 0:
            pin14.write_digital(1)
        else:
            pin14.write_digital(0)
        clk()
        b <<= 1

def set_color(r, g, b):
    send_byte(0)
    send_byte(0)
    send_byte(0)
    send_byte(0)
    prefix = 0b11000000
    if (b & 0x80) == 0:
        prefix |= 0b00100000
    if (b & 0x40) == 0:
        prefix |= 0b00010000
    if (g & 0x80) ==0:
        prefix |= 0b00001000
    if (g & 0x40) ==0:
        prefix |= 0b00000100
    if (r & 0x80) == 0:
        prefix |= 0b00000010
    if (r & 0x40) == 0:
        prefix |= 0b00000001

    to_send = [
        0, 0, 0, 0,
        prefix, r, g, b,
        0, 0, 0, 0
    ]
    for byte in to_send:
        send_byte(byte)

