from threading import Thread
import RPi.GPIO as GPIO

voltageMaps = {
    'HIGH': GPIO.HIGH,
    'LOW': GPIO.LOW
}

class SlaveController(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.pins = []

    def assignPins(self, pins = []):
        self.pins = pins
        for pin in pins:
            GPIO.setup(pin, GPIO.IN)

    def setPin(self, pin, voltage):
        GPIO.output(pin, voltageMaps[voltage])
