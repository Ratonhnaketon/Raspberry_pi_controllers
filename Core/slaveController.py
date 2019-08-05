from threading import Thread

voltageMaps = {
    'HIGH': GPIO.HIGH,
    'LOW': GPIO.LOW
}

def moduleExists(moduleName):
    try:
        __import__(moduleName)
    except ImportError:
        return False
    else:
        return True    

class SlaveController(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.pins = []

    def assignPins(self, pins = []):
        self.pins = pins
        if moduleExists('RPi.GPIO'):
            for pin in pins:
                RPi.GPIO.setup(pin, RPi.GPIO.IN)

    def setPin(self, pin, voltage):
        if not pin in self.pins:
            raise Exception('Pin {0} not set'.format(pin))

        if moduleExists('RPi.GPIO'):
            RPi.GPIO.output(pin, voltageMaps[voltage])
