/*
ver 1.0.0.61104
	- [ADD] UltraSonic and Motor controls
*/


#define UltraS_trigPin 7
#define UltraS_echoPin 6

#define Motor_button 3
#include "MotorDriver.h"
MotorDriver motor;
bool buttonOn;

void setup() {
	Serial.begin(9600);
	pinMode(UltraS_trigPin, OUTPUT);
	pinMode(UltraS_echoPin, INPUT);

	pinMode(Motor_button, INPUT_PULLUP);
	buttonOn = false;
	motor.begin();

}

long GetDistance() {
	long duration, Distance;
	digitalWrite(UltraS_trigPin, LOW);
	delayMicroseconds(2);
	digitalWrite(UltraS_trigPin, HIGH);
	delayMicroseconds(10);
	digitalWrite(UltraS_trigPin, LOW);
	duration = pulseIn(UltraS_echoPin, HIGH);
	Distance = (duration / 2) / 29.1;
	if (Distance >= 200 || Distance <= 0)
		return 10240;
	return Distance;
}


void Move(long leftSpeed, long rightSpeed) {
	const int leftMotor = 1;
	const int rightMotor = 0;
	if (leftSpeed == 0)
		motor.brake(leftMotor);
	else
		motor.speed(leftMotor, -leftSpeed);

	if (rightSpeed == 0)
		motor.brake(rightMotor);
	else
		motor.speed(rightMotor, -rightSpeed);
}
void Move(long singleSpeed) {
	Move(singleSpeed, singleSpeed);
}
void Stop() {
	Move(0);
}


void loop() {
	if (digitalRead(Motor_button) == LOW)
		buttonOn = !buttonOn;
	if (buttonOn) {
		if (GetDistance() < 50) {
			Stop();
		} else {
			Move(500, 500);
		}
	} else {
		Stop();
	}
}
