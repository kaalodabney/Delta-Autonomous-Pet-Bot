import time


class FatigueManager:
    startTime=time.time()
    fati=0
    
    ###### when fati ==0, it's not tired.#####

    def update(self, MotorOn):
        self.fatigueBasedOnTime()
        if MotorOn == 1: #self not needed since local variable
            self.fatigueBasedOnMotor()
        
    def fatigueBasedOnTime(self):
        if (time.time()-startTime) >=36:#change for demo?
            fati = fati-(1)
            startTime=time.time()
            if fati>100:
                fati=100
            if fati <0:
                fati=0
    
    def fatigueBasedOnMotor(self):
        fati=fati-0.002
        if fati>100:
            fati=100
        if fati <0:
            fati=0
                

    def getFatigueLevel(self):
        return fati
        
