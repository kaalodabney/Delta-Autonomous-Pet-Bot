import time

class SoundManager:
    sound=-1

    def update(self, fed, pet, us, ir, hunLevel):
        if pet == 1:
            self.sound=1
        elif fed == 1:
            self.sound=2
        elif hunLevel<=20 and int(hunLevel)%5==0:
            self.sound=3
        elif us<=10 or ir==1:
            self.sound=6
        else:
            self.sound = -1
        

    def getTune(self):
        print("sound: " + str(self.sound))
        return self.sound
