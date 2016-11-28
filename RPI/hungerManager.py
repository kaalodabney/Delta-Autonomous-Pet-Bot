
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
        self.hun=self.hun+30
        if self.hun>100:
            self.hun=100

    def hungerBasedOnTime(self):
        if (time.time()-self.startTime) >= 36: #change for demo?
            self.hun = self.hun-(1)
            self.startTime=time.time()
            if self.hun>100:
                self.hun=100
            if self.hun<0:
                self.hun = 0
     
                
    def hungerBasedOnMotor(self):
        self.hun = self.hun-0.001
        if self.hun>100:
            self.hun=100
        if self.hun<0:
            self.hun=0



    def calcHungerMod(self):
        if self.hun>=90:
            self.hunMod = 2
        if self.hun<90 and self.hun>=50:
            self.hunMod=1.5
        if self.hun<50:
            self.hunMod=1
            
    def getHungerLevel(self):
        return self.hun
   

    def getHungerMod(self):
        return self.hunMod

        
