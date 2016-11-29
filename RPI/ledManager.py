import time
import max7219.led as led
class LedManager:
    device = led.matrix(2)
    device.orientation(270)
    startTime = time.time()
    runningRoutine = 0

    happyFace = []
    defaultFace = []
    sadFace = []
    sadFace2 = []
    sleepingFace1 = []
    sleepingFace2 = []
    sleepingFace3 = []
    sleepingFace4 = []
    tiredFace = []
    hurtFace = []
    hurtFace2 = []

    def update(self, happyLevel, fatigueLevel, us, ir):
        if self.runningRoutine == 0:
            self.findRoutine()
        if self.runningRoutine == 1:
            self.setHappyFace()
        elif self.runningRoutine == 2:
            self.setDefaultFace()
        elif self.runningRoutine == 3:
            self.setSadFace()
        elif self.runningRoutine == 4:
            self.setTiredFace()
        elif self.runningRoutine == 5:
            self.setSleepingFace()
        elif self.runningRoutine == 6:
            self.setHurtFace()

    def findRoutine(self):
        self.runningRoutine = 1
        self.startTime = time.time()
	
    def test(self):
        for x in range(16):
            for y in range(8):
                time.sleep(0.05)
                self.device.pixel(x,y,1,redraw=True)

        for x in range(16):
            for y in range(8):
                time.sleep(0.05)
                self.device.pixel(x,y,0,redraw=True)

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
        
    def setHappyFace(self):
        for x in range(16):
            for y in range(8):
                self.device.pixel(x,y,self.happyFace[y][x],redraw=False)
        self.device.flush()

    def setDefaultFace(self):
        for x in range(16):
            for y in range(8):
                self.device.pixel(x,y,self.defaultFace[y][x],redraw=False)
        self.device.flush()

    def setSadFace(self):
        for x in range(16):
            for y in range(8):
                self.device.pixel(x,y,self.sadFace2[y][x],redraw=False)
        self.device.flush()

    def setSleepingFace(self):
        for x in range(16):
            for y in range(8):
                self.device.pixel(x,y,self.sleepingFace[y][x],redraw=False)
        self.device.flush()

    def setTiredFace(self):
        for x in range(16):
            for y in range(8):
                self.device.pixel(x,y,self.tiredFace[y][x],redraw=False)
        self.device.flush()

    def setHurtFace(self):
        for x in range(16):
            for y in range(8):
                self.device.pixel(x,y,self.hurtFace2[y][x],redraw=False)
        self.device.flush()

    def initFaces(self):
        self.happyFace = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0],
        [0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0],
        [0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0]]

        self.defaultFace = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0],
        [0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0],
        [0,0,1,0,1,0,1,0,0,1,0,1,0,1,0,0],
        [0,0,1,0,1,0,1,0,0,1,0,1,0,1,0,0],
        [0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0],
        [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

        self.sadFace = [
        [0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0],
        [0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,0],
        [1,1,0,0,0,1,0,0,0,0,1,0,0,0,1,1],
        [0,1,0,1,0,1,0,0,0,0,1,0,1,0,1,0],
        [0,1,0,0,0,1,0,0,0,0,1,0,0,0,1,0],
        [0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

        self.sadFace2 = [
        [0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0],
        [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,0,0,1,0,0,1,0,0,0,1,1,0],
        [0,0,1,0,1,0,1,0,0,1,0,1,0,1,0,0],
        [0,0,1,0,1,0,1,0,0,1,0,1,0,1,0,0],
        [0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0],
        [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

        self.sleepingFace1 = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0],
        [0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0],
        [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

        self.sleepingFace2 = [
        [0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0],
        [0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0],
        [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0]]

        self.sleepingFace3 = [
        [0,1,1,1,1,0,1,1,1,1,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0],
        [0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0],
        [0,1,1,1,1,0,1,1,1,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0],
        [0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0],
        [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0]]
        
        sleepingFace4 = [
        [0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0],
        [0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0],
        [0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0],
        [0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0],
        [0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0],
        [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0]]

        self.tiredFace = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0],
        [0,0,1,1,1,1,1,0,0,1,1,1,1,1,0,0],
        [0,0,1,1,1,1,1,0,0,1,1,1,1,1,0,0],
        [0,0,1,0,1,0,1,0,0,1,0,1,0,1,0,0],
        [0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0],
        [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

        self.hurtFace = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0],
        [0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0],
        [0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0],
        [0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0],
        [0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0],
        [0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

        self.hurtFace2 = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0],
        [0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0],
        [0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0],
        [0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0],
        [0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0],
        [0,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
