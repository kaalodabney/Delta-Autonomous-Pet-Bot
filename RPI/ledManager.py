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
            self.animateSleepingFace()
        elif self.runningRoutine == 6:
            self.setHurtFace()

    def findRoutine(self):
        self.runningRoutine = 5
        self.startTime = time.time()
	
    def animateSleepingFace(self):
        curTime = time.time()
        if(curTime - self.startTime) <= 1:
            self.setSleepingFace1()
        elif 1 < (curTime - self.startTime) <= 2:
            self.setSleepingFace2()
        elif 2 < (curTime - self.startTime) <= 3:
            self.setSleepingFace3()
        elif 3 < (curTime - self.startTime) <=4:
            self.setSleepingFace4()
        
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

    def setSleepingFace1(self):
        for x in range(16):
            for y in range(8):
                self.device.pixel(x,y,self.sleepingFace1[y][x],redraw=False)
        self.device.flush()

    def setSleepingFace2(self):
        for x in range(16):
            for y in range(8):
                self.device.pixel(x,y,self.sleepingFace2[y][x],redraw=False)
        self.device.flush()

    def setSleepingFace3(self):
        for x in range(16):
            for y in range(8):
                self.device.pixel(x,y,self.sleepingFace3[y][x],redraw=False)
        self.device.flush()

    def setSleepingFace4(self):
        for x in range(16):
            for y in range(8):
                self.device.pixel(x,y,self.sleepingFace4[y][x],redraw=False)
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

    def allOn(self):
        for x in range(16):
            for y in range(8):
                self.device.pixel(x,y,1,redraw=False)
        self.device.flush()

    def allOff(self):
        for x in range(16):
            for y in range(8):
                self.device.pixel(x,y,0,redraw=False)
        self.device.flush()

    def allOffNoFlush(self):
        for x in range(16):
            for y in range(8):
                self.device.pixel(x,y,0,redraw=False)

    def test(self):
        for x in range(16):
            for y in range(8):
                time.sleep(0.05)
                self.device.pixel(x,y,1,redraw=True)

        for x in range(16):
            for y in range(8):
                time.sleep(0.05)
                self.device.pixel(x,y,0,redraw=True)

    def flashTest(self):
        curTime = time.time()
        if (curTime - self.startTime) <= 1:
            self.device.brightness(0)
            self.allOn()
        elif 1 < (curTime - self.startTime) <= 1.5:
            self.allOff()
        elif 1.5 < (curTime - self.startTime) <= 2.5:
            self.device.brightness(15)
            self.allOn()
        else:
            self.allOff()
            self.runningRoutine = 0

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
