#pylint: disable=import-error
from microbit import *
from microbit import uart

START_BYTE = 0x7E
VERSION = 0xFF
STOP_BYTE = 0xEF

class MP3Player:
    def __init__(self, tx, rx):
        uart.init(tx=tx, rx=rx, baudrate=9600)

    def _send_byte(self, byte):
        uart.write(byte)

    def _send_bytes(self, byte_array):
        for byte in byte_array:
            self._send_byte(byte)

    def _send_command(self, command, data1=0, data2=0, feedback=False):
        data = [START_BYTE,
                VERSION,
                5,
                command,
                1 if feedback else 0,
                data1,
                data2,
                STOP_BYTE]
        self._send_bytes(data)

    def play_track(self):
        self._send_command(0x03)

    def next(self):
        self._send_command(0x01)

    def prev(self):
        self._send_command(0x02)

    def volume_up(self):
        self._send_command(0x04)

    def volume_down(self):
        self._send_command(0x05)

    def set_volume(self, volume=15):
        '''
        Set volume - 0-30
        '''
        self._send_command(0x05, 0, volume)

    def set_equalizer(self, equalizer):
        '''
        Set the equalizer:
            0: Normal
            1: Pop
            2: Rock
            3: Jazz
            4: Classic
            5: Bass
        '''
        self._send_command(0x07, 0, equalizer)

    def restart(self):
        self._send_command(0x08)

    def standby(self):
        self._send_command(0x0A)

    def play(self):
        '''
        Play the current track
        '''
        self._send_command(0x0D)

    def pause(self):
        '''
        Pause the current track
        '''
        self._send_command(0x0E)

    def set_folder(self, folder):
        # TODO
        self._send_command(0x0F)

    def repeat_all(self, value):
        self._send_command(0x11, 0, 1 if value else 0)

    def repeat_one(self):
        self._send_command(0x19)

    def stop(self):
        self._send_command(0x16)
