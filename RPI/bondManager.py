import time


class BondManager:
    bon=100
    bonMod=100

    #### if bon == 100 then pet loves you ####

    def update(self, happMod, pet, fed):
        if pet==1:
            self.bondBasedOnPet()
        if fed ==1:
            self.bondBasedOnFed()
        self.bondBasedOnTime(happMod)


    def bondBasedOnPet(self):
        bon = bon + 3
        if bon>100:
            bon=100
        if bon<0:
            bon=0

    def bondBasedOnFed(self):
        bon = bon + 2
        if bon>100:
            bon=100
        if bon<0:
            bon=0


    def bondBasedOnTime(self, happMod):
        if (time.time()-startTime) >= 36:
            bon = bon-(1/happMod)
            startTime=time.time()
            if bon>100:
                bon=100
            if bon<0:
                bon=0

    def getBondLevel(self):
        return bon

        
