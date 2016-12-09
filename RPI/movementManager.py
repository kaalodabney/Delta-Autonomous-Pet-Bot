import time
import random

class MovementManager:
    runningRoutine = 0;
    #Used to identify the routines to run
    #0 none (used to indicate no routine running)
    #1 rest
    #2 moveRandom
    #3 moveSpiral
    #4 back and forth (reaction when fed, overrides 1-3)
    #5 wiggle (reaction when pat, overrides 1-3)
    #6 spin (saved for if we implement bonding level)
    startTime = time.time();
    duration = 0;
    step = -1;
    avoidOn = False;
    avoidStartTime = 0;
    avoidDuration = 0;
    avoidStep = -1;
    motor1 = 0          #value to send to arduino to run motors
    motor2 = 0          #value to send to arduino to run motors
    motorState = False  #true if motor was ran last loop, false if not, used for hunger
    isSleeping = False  #true if currently resting, used to for led
    deepSleep = False   #true if sleeping when fatigue is below 20, sleeps until fatigue up to 80


    def updateShow(self,fed,pat):
        if(fed == 1):
            self.setRoutine(4)
            self.startTime = time.time()
        elif(pat == 1):
            self.setRoutine(5)
            self.startTime = time.time()
        self.runRoutineShow();


    def update(self,happyLevel,bondLevel,fatigue,uSensor,irSensor,fed,pat):
        print("move routine: " + str(self.runningRoutine))
        if(self.deepSleep == True):
           print("deep sleep")
           self.setRoutine(1);
           if(fatigue > 80):
             self.deepSleep = False
        if(self.runningRoutine == 0):
            self.findRoutine(happyLevel,fed,pat)
        elif(fatigue<20):
            self.deepSleep = True
            self.setRoutine(1);
        elif(fed==1):
            self.setRoutine(4);
        elif(pat==1):
            if(bondLevel>70) & (random.random()>.6):
                self.setRoutine(6);
            else:
                self.setRoutine(5);        
        self.runRoutine(fatigue,uSensor,irSensor);

    def runRoutineShow(self):
        self.motorState= True
        self.isSleeping=False
        if self.runningRoutine == 4:
            self.rFwdBckShow()
        elif self.runningRoutine == 5:
            self.rWiggle(100)

    def runRoutine(self,fatigue,uSensor,irSensor):
        self.isSleeping=False
        if((uSensor < 20) | (irSensor == 1)):
            self.avoidOn = True

        if(self.avoidOn==True):
            self.avoidCollision(fatigue);

        elif(self.runningRoutine==1):
            self.rRest(fatigue);
            self.isSleeping = True

        elif(self.runningRoutine==2):
            self.rRandom(fatigue);

        elif(self.runningRoutine==3):
            self.rSpiral(fatigue);

        elif(self.runningRoutine==4):
            self.rFwdBck(fatigue);

        elif(self.runningRoutine==5):
            self.rWiggle(fatigue);

        elif(self.runningRoutine==6):
            self.rSpin(fatigue);
    
    def setRoutine(self, routine):
        self.runningRoutine=routine;
        self.step=-1;
        
    def findRoutine(self,happyLevel,fed,pat):
        r = random.random()*6;
        if(r<2):
            self.setRoutine(1);
        elif (happyLevel>80) & (r<3):
            self.setRoutine(3);
        else:
            self.setRoutine(2);

    def initRoutine(self):
        self.duration = 0;
        self.step = 0;
        self.startTime = time.time();
    
    def setMotors(self,s1,s2,fatigue):
        self.motor1=((5/100)*fatigue)*s1
        self.motor2=((5/100)*fatigue)*s2
       
        #for some reason even numbers drive backwards and odd numbers drive forwards
        if(self.motor1 > 0 & (self.motor1 % 2 == 0)):
            print("even to odd")
            self.motor1 += 1
        elif(self.motor1 < 0 & (self.motor1 % 2 == 1)):
            print("odd to even")
            self.motor1 -= 1    

        if(self.motor2 > 0 & (self.motor2 % 2 == 0)):
            self.motor2 += 1
        elif(self.motor2 < 0 & (self.motor2 % 2 == 1)):
            self.motor2 -= 1  


        if (s1 > 0) & (s2 > 0):
            self.motorState = False
        else:
            self.motorState = True

    def setMotorsShow(self,s1,s2):
        self.motor1 = s1
        self.motor2 = s2
        
    def getIsSleeping(self):
        return self.isSleeping

    def getMotorState(self):
        return self.motorState;

    def getMotor1Value(self):
        return self.motor1;

    def getMotor2Value(self): 
        return self.motor2;
    
    def avoidCollision(self, fatigue):
        if(self.avoidStep == -1):
            self.setMotors(-1,-1,fatigue);
            self.avoidDuration = 1;
            self.avoidStartTime = time.time();
            self.avoidStep+=1;
        elif(self.avoidStep==0):
            if(time.time()-self.avoidStartTime > self.avoidDuration):
                self.setMotors(1,-1,fatigue);
                self.avoidDuration+=1.5;
                self.avoidStep+=1;
        elif(self.avoidStep==1):
            if(time.time()-self.avoidStartTime > self.avoidDuration):
                self.setMotors(0,0,fatigue);
                self.avoidStep=-1;
                self.avoidDuration=0;
                self.avoidOn=False;
                self.duration += (time.time()-self.avoidStartTime);

    ############################
    #Routines:                 #
    ############################

    def rRest(self,fatigue):
        if(self.step == -1):
            self.initRoutine();
            self.duration = random.random()*15+5;
            self.setMotors(0,0,fatigue);
        elif(time.time()-self.startTime>self.duration):
            self.setRoutine(0);
        
    def rRandom(self,fatigue):
        if(self.step == -1):
            self.initRoutine();
            self.duration = random.random()*4;
            if(random.random()>.5):
                self.setMotors(-100,100,fatigue);
            else:
                self.setMotors(1,-1,fatigue);
        elif(self.step == 0):
            if(time.time()-self.startTime>self.duration):
                self.duration += random.random()*10;
                self.setMotors(1,1,fatigue);
                self.step+=1;
        elif(self.step == 1):
            if(time.time()-self.startTime>self.duration):
                self.setRoutine(0);

    def rSpiral(self,fatigue):
        if(self.step == -1):
            self.initRoutine();
            self.duration = random.random()*10;
            self.setMotors(.8,1,fatigue);
        elif(time.time()-self.startTime>self.duration):
            self.setRoutine(0);
            
    def rFwdBck(self,fatigue): 
        if(self.step == -1):
            self.initRoutine();
            self.duration = .4;
            self.setMotors(1,1,fatigue);
        elif(self.step > 4):
            self.setRoutine(0);
        elif(self.step%2 == 0):
            if(time.time()-self.startTime>self.duration):
                self.duration += .4;
                self.setMotors(-1,-1,fatigue);
                self.step+=1;
        elif(self.step%2 == 1):
            if(time.time()-self.startTime>self.duration):
                self.duration += .4;
                self.setMotors(1,1,fatigue);
                self.step+=1;

    def rFwdBckShow(self):
        curTime = time.time()
        if(curTime - self.startTime) <= .3:
            self.setMotorsShow(20,20)
        elif .3 < (curTime - self.startTime) <= .6:
            self.setMotorsShow(-20,-20)
        elif .6 < (curTime - self.startTime) <=.9:
            self.setMotorsShow(20,20)
        elif .9 < (curTime - self.startTime):
            self.setMotorsShow(0,0)
            self.setRoutine(0)
                
    def rWiggle(self,fatigue):
        if(self.step == -1):
            self.initRoutine();
            self.duration = .5;
            self.setMotors(1,-1,fatigue);
        elif(self.step > 4):
            self.setRoutine(0);
        elif(self.step%2 == 0):
            if(time.time()-self.startTime>self.duration):
                self.duration += .75;
                self.setMotors(-100,100,fatigue);
                self.step+=1;
        elif(self.step%2 == 1):
            if(time.time()-self.startTime>self.duration):
                self.duration += .75;
                self.setMotors(100,-100,fatigue);
                self.step+=1;
            
    def rSpin(self,fatigue):
        if(self.step == -1):
            self.initRoutine();
            self.duration = random.random()*3+2; ##maybe test to make it turn back to you?(use * then)
            if(random.random()>.5):
                self.setMotors(1,-1,fatigue);
            else:
                self.setMotors(-1,1,fatigue);
        elif(time.time()-self.startTime>self.duration):
            self.setRoutine(0);
