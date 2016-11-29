import time


class HappyManager:
    happ = 100
    happMod=100
    startTime = time.time()

    ###### if happpy == 100, pet is totally happy ######
    
    def update(self, hunMod, pet):
        self.happyBasedOnTime(hunMod)
        if pet==1:
            self.happyBasedOnPet()
        self.calcHappyMod()


    def happyBasedOnTime(self, hunMod):
        if (time.time()-self.startTime) >=36:#change for demo?
            self.happ = self.happ-(1/hunMod)
            self.startTime=time.time()
            if self.happ>100:
                self.happ=100
            if self.happ <0:
                self.happ=0
                
        
    def happyBasedOnPet(self):
        self.happ = self.happ + (5)
        if self.happ>100:
            self.happ=100
            
        

    def calcHappyMod(self):
        if self.happ>=90:
            self.happMod = 2
        if self.happ<90 and self.happ>=50:
            self.happMod=1.5
        if self.happ<50:
            self.happMod=1
            
    def getHappyLevel(self):
        return self.happ

    def getHappyMod(self):
        return self.happMod


            
