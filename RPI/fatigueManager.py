import time


class FatigueManager:
    startTime=time.time()
    fati=100
    
    ###### when fati == 100 it is completly awake.#####

    def update(self, MotorOn, isSleeping):
        self.fatigueBasedOnTime(isSleeping)
        if MotorOn == 1: #self not needed since local variable
            self.fatigueBasedOnMotor()
        
    def fatigueBasedOnTime(self, isSleeping):
        if (time.time()-self.startTime) >=1:#change for demo? was 36
            if isSleeping == False:
                self.fati = self.fati-(1)
            else:
                self.fati = self.fati + 5
            self.startTime=time.time()
            if self.fati>100:
                self.fati=100
            if self.fati <0:
                self.fati=0
    
    def fatigueBasedOnMotor(self):
        self.fati = self.fati-0.002
        if self.fati>100:
            self.fati=100
        if self.fati <0:
            self.fati=0
                

    def getFatigueLevel(self):
        return self.fati
        
