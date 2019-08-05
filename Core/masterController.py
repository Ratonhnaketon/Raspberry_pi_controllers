from threading import Thread

class MasterController(Thread):
    def __init__(self):
        Thread.__init__(self)