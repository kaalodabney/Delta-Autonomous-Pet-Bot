import time

class SoundManager:
    sound=0

    def update(self, pet, fed, ir, us, hunLevel):
        if pet==1:
            sound=1
        if fed ==1:
            sound=2
        if hunLevel<=20 and int(hunLevel)%5==0:
            sound=3
        if us==10 or ir==1:
            sound=4
        

        def getSoundMod:
            return self.sound
