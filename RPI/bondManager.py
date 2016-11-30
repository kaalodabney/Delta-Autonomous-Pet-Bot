import time


class BondManager:
    bon=0
    bonMod=100
    startTime = time.time()

    #### if bon == 100 then pet loves you ####

    def update(self, happMod, pet, fed):
        if pet==1:
            self.bondBasedOnPet()
        if fed ==1:
            self.bondBasedOnFed()
        self.bondBasedOnTime(happMod)


    def bondBasedOnPet(self):
        self.bon = self.bon + 3
        if self.bon>100:
            self.bon=100
        if self.bon<0:
            self.bon=0

    def bondBasedOnFed(self):
        self.bon = self.bon + 2
        if self.bon>100:
            self.bon=100
        if self.bon<0:
            self.bon=0


    def bondBasedOnTime(self, happMod):
        if (time.time()-self.startTime) >= 36:
            self.bon = self.bon-(1/happMod)
            self.startTime=time.time()
            if self.bon>100:
                self.bon=100
            if self.bon<0:
                self.bon=0

    def getBondLevel(self):
        return self.bon

        
