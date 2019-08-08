from threading import Thread
import RPi.GPIO as GPIO 

voltageMaps = {
    'HIGH': GPIO.HIGH,
    'LOW': GPIO.LOW
}

class SlaveController(Thread):
    def __init__(self):
        Thread.__init__(self, controllerType)
        self.daemon = True
        self.controllerType = GPIO.IN if 'IN' else GPIO.OUT  
        self.pins = []

    def assignPins(self, pins = []):
        self.pins = pins
        if moduleExists('RPi.GPIO'):
            for pin in pins:
                GPIO.setup(pin, self.controllerType)

    def setPin(self, pin, voltage):
        if not pin in self.pins:
            raise Exception('Pin {0} not set'.format(pin))

        if self.controllerType == 'IN':
            GPIO.input(pin, voltageMaps[voltage])
        else:
            GPIO.output(pin, voltageMaps[voltage])
