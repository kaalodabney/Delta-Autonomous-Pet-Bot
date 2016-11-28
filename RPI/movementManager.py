import time

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
    avoidOn = false;
    avoidStartTime = 0;
    avoidDuration = 0;
    avoidStep = -1;
    motor1 = 0          #value to send to arduino to run motors
    motor2 = 0          #value to send to arduino to run motors
    motorState = false     #true if motor was ran last loop, false if not used for hunger

    def update(self,happyLevel,bondLevel,uSensor,irSensor,fatigue,fed,pat):
        if(runningRoutine==0):
            findRoutine(self,happyLevel,fed,pat)
        elif(fatigue<20):
            setRoutine(self,1);
        elif(fed==true):
            setRoutine(self,4);
        elif(pat==true):
            if(bondLevel>70 & random()>.6):
                setRoutine(self,6);
            else:
                setRoutine(self,5);        
        runRoutine(self,fatigue,uSensor,irSensor);

    def runRoutine(self,fatigue,uSensor,irSensor):
        if(avoidOn==true):
            avoidCollision(self);
        elif(runningRoutine==1):
            rRest(self,fatigue);
        elif(runningRoutine==2):
            if(uSensor>10 | irSensor==true):
                avoidOn=true;
            rRandom(self,fatigue);
        elif(runningRoutine==3):
            if(uSensor>10 | irSensor==true):
                avoidOn=true;
            rSpiral(self,fatigue);
        elif(runningRoutine==4):
            rFwdBck(self,fatigue);
        elif(runningRoutine==5):
            rWiggle(self,fatigue);
        elif(runningRoutine==6):
            rSpin(self,fatigue);
    
    def setRoutine(self, routine):
        runningRoutine=routine;
        step=-1;
        
    def findRoutine(self,happyLevel,fed,pat):
        r = random()*6;
        if(r<2):
            setRoutine(self,1);
        elif(happyLevel>80 & r<3):
            setRoutine(self,3);
        else:
            setRoutine(self,2);

    def initRoutine(self):
        duration = 0;
        step = 0;
        startTime = time.time();
    
    def setMotors(self,s1,s2,fatigue):
        motor1=(s1/100*fatigue/100)*25+75;
        motor2=(s2/100*fatigue/100)*25+75;
        
    def getMotorState(self):
        return motorState;

    def getMotor1Value(self):
        return motor1;

    def getMotor2Value(self): 
        return motor2;
    
    def avoidCollision(self):
        if(avoidStep == -1):
            setMotors(self,-10,-10);
            avoidDuration = 1;
            avoidStartTime = time.time();
            avoidStep+=1;
        elif(avoidStep==0):
            if(time.time()-avoidStartTime > avoidDuration):
                setMotors(self,100,-100);
                avoidDuration+=.5;
                avoidStep+=1;
        elif(avoidStep==1):
            if(time.time()-avoidStartTime > avoidDuration):
                setMotors(self,0,0);
                avoidStep=-1;
                avoidDuration=0;
                avoidOn=false;
                duration += (time.time()-avoidStartTime);

    ############################
    #Routines:                 #
    ############################

    def rRest(self,fatigue):
        if(step == -1):
            initRoutine(self);
            duration = random()*15+5;
            setMotors(self,0,0,fatigue);
            motorState = false;
        elif(time.time()-startTime>duration):
            setRoutine(self,0);
        
    def rRandom(self,fatigue):
        if(step == -1):
            initRoutine(self);
            duration = random()*4;
            if(random()>.5):
                setMotors(self,-100,100,fatigue);
            else:
                setMotors(self,100,-100,fatigue);
        elif(step == 0):
            if(time.time()-startTime>duration):
                duration += random()*15+5;
                setMotors(self,100,100,fatigue);
                step+=1;
        elif(step == 1):
            if(time.time()-startTime>duration):
                setRoutine(self,0);

    def rSpiral(self,fatigue):
        if(step == -1):
            initRoutine(self);
            duration = random()*15+5;
            setMotors(self,50,70,fatigue);
            motorState = false;
        elif(time.time()-startTime>duration):
            setRoutine(self,0);
            
    def rFwdBck(self,fatigue): 
        if(step == -1):
            initRoutine(self);
            duration = .8;
            setMotors(self,90,90,fatigue);
        elif(step > 4):
            setRoutine(self,0);
        elif(step%2 == 0):
            if(time.time()-startTime>duration):
                duration += .8;
                setMotors(self,-95,-95,fatigue);
                step+=1;
        elif(step%2 == 1):
            if(time.time()-startTime>duration):
                duration += .8;
                setMotors(self,95,95,fatigue);
                step+=1;
                
    def rWiggle(self,fatigue):
        if(step == -1):
            initRoutine(self);
            duration = .75;
            setMotors(self,80,-80,fatigue);
        elif(step > 4):
            setRoutine(self,0);
        elif(step%2 == 0):
            if(time.time()-startTime>duration):
                duration += .75;
                setMotors(self,80,-80,fatigue);
                step+=1;
        elif(step%2 == 1):
            if(time.time()-startTime>duration):
                duration += .75;
                setMotors(self,-95,95,fatigue);
                step+=1;
            
    def rSpin(self,fatigue):
        if(step == -1):
            initRoutine(self);
            duration = random()*3+2; ##maybe test to make it turn back to you?(use * then)
            if(random()>.5):
                setMotors(self,95,-95,fatigue);
            else:
                setMotors(self,-95,95,fatigue);
        elif(time.time()-startTime>duration):
            setRoutine(self,0);
    
