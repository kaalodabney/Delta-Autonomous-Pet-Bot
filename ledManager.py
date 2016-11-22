import time
import max7219.led as led

class LedManager:
    device = led.matrix(2)
    device.orientation(270)
    startTime = time.time()
    runningRoutine = 0

    def update(self):
	if self.runningRoutine == 0:
            self.findRoutine()
        elif self.runningRoutine == 1:
            self.flash()

    def findRoutine(self):
	self.runningRoutine = 1
        self.startTime = time.time()
	
    def test(self):
        for x in range(16):
            for y in range(8):
                time.sleep(0.05)
                device.pixel(x,y,1,redraw=True)

        for x in range(16):
            for y in range(8):
                time.sleep(0.05)
                device.pixel(x,y,0,redraw=True)

    def flash(self):
	curTime = time.time()
        if (curTime - self.startTime) <= 1:
            self.device.brightness(0)
	    self.flashOn()
        elif 1 < (curTime - self.startTime) <= 1.5:
            self.flashOff()
        elif 1.5 < (curTime - self.startTime) <= 2.5:
            self.device.brightness(15)
	    self.flashOn()
        else:
            self.flashOff()
            self.runningRoutine = 0

    def flashOn(self):
        for x in range(16):
            for y in range(8):
                self.device.pixel(x,y,1,redraw=False)
        self.device.flush()

    def flashOff(self):
        for x in range(16):
            for y in range(8):
                self.device.pixel(x,y,0,redraw=False)
        self.device.flush()
        

