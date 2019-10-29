from microbit import *
import utime

def list_to_binary(l):
    '''Convert a list of booleans to a binary number'''
    return int('0b' + ''.join('1' if x else '0' for x in l), 2)

def pulse_in(pin):
    while pin.read_digital():
        pass
    while not pin.read_digital():
        pass
    a = utime.ticks_us()
    while pin.read_digital():
        pass
    return utime.ticks_diff(utime.ticks_us(), a)


class DHTSensor:
    '''Interface with the DHT11 Temperature and Humidity Sensor'''
    def __init__(self, pin):
        self.pin = pin
        self.pin.write_digital(1)

    def read(self):
        '''Read data from the DHT11 sensor

        Returns tuple (temperature, humidity) or False if error
        '''
        print(":: start read")
        data_array = [False for i in range(40)]
        result_array = [0 for i in range(5)]
        self.pin.write_digital(0)
        sleep(18)
        self.pin.write_digital(1)
        self.pin.set_pull(self.pin.PULL_DOWN)

        self.pin.read_digital()

        start = utime.ticks_us()
        while self.pin.read_digital():
            pass
        while not self.pin.read_digital():
            pass
        while self.pin.read_digital():
            pass
        d = utime.ticks_diff(utime.ticks_us(), start)
        print(d)

        for i in range(40):
            while not self.pin.read_digital():
                pass
            if self.pin.read_digital():
                data_array[i] = True
            while self.pin.read_digital():
                pass

        print(":: read, parsing", data_array)

        data = [
            list_to_binary(data_array[x * 8:(x + 1) * 8])
            for x in range(5)
        ]

        print(":: done, got", data)

        data_sum = sum(data[:4])
        checksum = data[4]


        if data_sum > 512:
            data_sum -= 512
        if data_sum > 256:
            data_sum -= 256

        print(":: sum = {}, checksum {}".format(
            data_sum, checksum
        ))

        if data_sum == checksum:
            return (result_array[0] + result_array[1] / 100,
                    result_array[2] + result_array[3] / 100)
        else:
            return False

dht = DHTSensor(pin0)

while True:
    print(dht.read())
