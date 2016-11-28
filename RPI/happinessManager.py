import time


class HappyManager:
    happ = 100
    happMod=100

    ###### if happpy == 100, pet is totally happy ######
    
    def update(self, hunMod, pet):
        self.happyBasedOnTime(hunMod)
        if pet==1:
            self.happyBasedOnPet()
        self.calcHappyMod()


    def happyBasedOnTime(self, hunMod):
        if (time.time()-startTime) >=36:#change for demo?
            happ = happ-(1/hunMod)
            startTime=time.time()
            if happ>100:
                happ=100
            if happ <0:
                happ=0
                
        
    def happyBasedOnPet(self):
        happ = happ + (5)
        if happ>100:
            happ=100
            
        

    def calcHappyMod(self):
        if happ>=90:
            happMod = 2
        if happ<90 and happ>=50:
            happMod=1.5
        if happ<50:
            happMod=1
            
    def getHappyLevel(self):
        return happ

    def getHappyMod(self):
        return happMod


            
