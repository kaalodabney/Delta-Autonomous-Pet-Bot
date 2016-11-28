#include "MotorDriver.h"
#define rightMotor 0;
#define leftMotor 1;
MotorDriver motor;

#define trigPin 7
#define echoPin 6

#define soundPin 2

#define btnStart 3
bool btnStartOn;
bool btnStartHeld;

void setup() {
	Serial.begin(9600);
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
