from led import main as led
from temperatura import main as temperatura
from ultrasonico import main as ultrasonico

import RPi.GPIO as GPIO
import time

class Sensores:
    def __init__(self, key):
        # Configurar pines según la clave
        if key == "led":
            self.sensor = Led()
        elif key == "ultrasonico":
            self.sensor = Ultrasonico()
        elif key == "temperatura":
            self.sensor = Temperatura()

    def leer(self):
        return self.sensor.leer()

class Led:
    def __init__(self, pin=22):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

    def leer(self):
        GPIO.output(self.pin, True)
        time.sleep(1)
        GPIO.output(self.pin, False)

class Ultrasonico:
    def __init__(self, trig_pin=23, echo_pin=24):
        self.trig_pin = trig_pin
        self.echo_pin = echo_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trig_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)

    def leer(self):
        GPIO.output(self.trig_pin, True)
        time.sleep(0.00001)
        GPIO.output(self.trig_pin, False)
        while GPIO.input(self.echo_pin) == 0:
            start_time = time.time()
        while GPIO.input(self.echo_pin) == 1:
            end_time = time.time()
        duration = end_time - start_time
        distance = duration * 17150
        return distance

class Temperatura:
    def __init__(self, hum_pin=4):
        self.hum_pin = hum_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.hum_pin, GPIO.IN)

    def leer(self):
        humidity = GPIO.input(self.hum_pin)
        return humidity
