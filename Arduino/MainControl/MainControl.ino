#include "MotorDriver.h"
#define rightMotor 0
#define leftMotor 1
MotorDriver motor;

#define trigPin 7
#define echoPin 6

#define soundPin 2

#define btnStart 3

bool btnStartOn;
bool btnStartHeld;

unsigned long serialData = 0;
int inByte;
int motorDataInL;
int motorDataInR;
char soundDataIn;
bool fedDataOut;
bool patDataOut;
bool motorStateDataOut;
long ultraSonicDataOut;
long irDataOut;

int songTone[3][10] = { { 300, 300 }, { 777, 400 }, { 4000, 2000, 1000 } };
int songTone_Length[3] = { 2, 2, 3 };
//const int songTone_Length[3] and songTone???????
const int s_error = 0;
const int s_hello = 1;
const int s_bye = 2;
const int eachToneLastMS = 2000;
int tone_StartTime = 0;
int soundIndex_Playing = -1;
int toneIndex_Playing = 0;


void setup() {
  Serial.begin(9600);
  while(!Serial){
    
  }
	pinMode(trigPin, OUTPUT);
	pinMode(echoPin, INPUT);
	pinMode(btnStart, INPUT_PULLUP);

	//pinMode(led, OUTPUT);
	//pinMode(led2, OUTPUT);

	btnStartOn = false;
	btnStartHeld = false;
	motor.begin();
}

//long inputArr[];
//long outputArr[];
void loop() {
	if (digitalRead(btnStart) == LOW) {
		if (!btnStartHeld) {
			btnStartOn = !btnStartOn;
			btnStartHeld = true;
		}
	} else {
		btnStartHeld = false;
	}

	if (btnStartOn) {
		if (GetDistance() < 50) {
			PlaySound(s_hello, true);
			Move(-200, -200);
		} else {
			PlaySound(s_bye, true);
			Move(100, 100);
		}
	} else {
		Stop();
	}
	PlayTone();
}

void PlayTone() {
	if (soundIndex_Playing < 0)
		//NOT playing
		return;

	if (tone_StartTime == 0) {
		tone_StartTime = millis();
		tone(soundPin, songTone[soundIndex_Playing][toneIndex_Playing]);
	} else if (millis() - tone_StartTime >= eachToneLastMS) {
		tone_StartTime = 0;
		noTone(soundPin);
		if (++toneIndex_Playing < songTone_Length[soundIndex_Playing])
			PlayTone();
		else
			soundIndex_Playing = -1;
	}
}

void PlaySound(int newSoundIndex, bool InterruptCurrPlaying) {
	if (soundIndex_Playing >= 0) {
		//is playing
		if (InterruptCurrPlaying == false)
			//NOT allowed to interrupt current playing
			return;
		else if (InterruptCurrPlaying == true && newSoundIndex == soundIndex_Playing)
			//allowed to interrupt, but will NOT interrupt because the same sound is playing
			return;
		else if (InterruptCurrPlaying == true)
			//will interrupt current playing
			noTone(soundPin);
	}
	soundIndex_Playing = newSoundIndex;
	toneIndex_Playing = 0;
	tone_StartTime = 0;
}



long GetDistance() {
	long duration, Distance;
	digitalWrite(trigPin, LOW);  // Added this line
	delayMicroseconds(2); // Added this line
	digitalWrite(trigPin, HIGH);
	delayMicroseconds(10); // Added this line
	digitalWrite(trigPin, LOW);
	duration = pulseIn(echoPin, HIGH);
	Distance = (duration / 2) / 29.1;
	if (Distance >= 200 || Distance <= 0)
		return 9999;
	return Distance;
}



void MoveLeft(long speedX) {
	if (speedX == 0)
		motor.brake(leftMotor);
	else
		motor.speed(leftMotor, -speedX);
}
void MoveRight(long speedX) {
	if (speedX == 0)
		motor.brake(rightMotor);
	else
		motor.speed(rightMotor, -speedX);
}

void Move(long leftSpeed, long rightSpeed) {
	MoveLeft(leftSpeed);
	MoveRight(rightSpeed);
}

void Move(long singleSpeed) {
	Move(singleSpeed, singleSpeed);
}

void Stop() {
	Move(0);
}

void getSerial() {
  serialData = 0;
  while (inByte != '/') {
    inByte = Serial.read();
    if(inByte > 0 && inByte != '/') {
      serialData = serialData * 10 + inByte - '0';
    }
  }  
  inByte = 0;
  return serialData;
}

//called at the start of loop to read data from the Raspberry pi, dictates motor speeds and tunes played
void readDataIn(){
  while(Serial.available() > 0){
    getSerial();
    switch(serialData){
      //data for left motor
      case 1:
        {
          getSerial();
          motorDataInL = serialData;
          break;
        }
      case 2:
        {
          getSerial();
          motorDataInR = serialData;
          break;
        }
      case 3: 
        {
          getSerial();
          soundDataIn = char(serialData);
          break;
        }
    }
  }
}


//called at end of loop to send data to the raspberry pi for the AI to determine what to do next loop
void sendDataOut(){ 
  int err;
  char dataOut[50];
  err = sprintf(dataOut, "1/%c/2/%c/3/%c/4/%d/5/%d/", char(fedDataOut), char(patDataOut), char(motorStateDataOut), ultraSonicDataOut, irDataOut);
  if(err < 0)
    Serial.write("0/");
  else
    Serial.write(dataOut);
}


