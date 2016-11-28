import time


class HungerManager:
    startTime=time.time()
    hun = 100
    hunMod = 100
    
    ####### when hun==100, means it's fed and not hungry #######

    def update(self, fed, MotorOn):
        if fed ==1:
            self.fedButtonPush()
        if MotorOn==1:
            self.hungerBasedOnMotor()
        self.hungerBasedOnTime()
        self.calcHungerMod()
        

    def fedButtonPush(self):
        hun=hun+30
        if hun>100:
            hun=100

    def hungerBasedOnTime(self):
        if (time.time()-startTime) >= 36: #change for demo?
            hun = hun-(1)
            startTime=time.time()
            if hun>100:
                hun=100
            if hum<0:
                hun = 0
     
                
    def hungerBasedOnMotor(self):
        hun = hun-0.001
        if hun>100:
            hun=100
        if hun<0:
            hun=0



    def calcHungerMod(self):
        if hun>=90:
            hunMod = 2
        if hun<90 and hun>=50:
            hunMod=1.5
        if hun<50:
            hunMod=1
            
    def getHungerLevel(self):
        return hun
   

    def getHungerMod(self):
        return hunMod

        
