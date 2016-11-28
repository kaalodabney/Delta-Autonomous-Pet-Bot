#include "MotorDriver.h"

//declare analog pins
int IRsensorPin = A0;    	// select the input pin for the IR sensor
//declare digital pins
int USsensorTRIGPin = 7;	// select the input pin for the US TRIG pin
int USsensorECHOPin = 6;	// select the input pin for the US ECHO pin
int buttonPin1 = 5;			// select the input pin for button 1
int buttonPin2 = 4;			// select the input pin for button 2
int buttonPin3 = 3;			// select the input pin for button 3
int speakerPin = 2;			// select the input pin for the speaker

//declare motor pins
int leftMotor = 1;
int rightMotor = 0;

//initialize input pins
int IRsensorValue = 0;
int USsensorValue = 0;
int button1State = HIGH;
int button2State = HIGH;
int button3State = HIGH;

void setup() {
	// set the pins
	pinMode(IRsensorPin, INPUT);
	pinMode(USsensorTRIGPin, OUTPUT);
	pinMode(USsensorECHOPin, INPUT);
	pinMode(buttonPin1, INPUT_PULLUP);
	pinMode(buttonPin2, INPUT_PULLUP);
	pinMode(buttonPin3, INPUT_PULLUP);
	pinMode(speakerPin, OUTPUT);
	
	//open serial port
	Serial.begin(9600);
	motor.begin();
}

void loop() {
	// read the value from the IR sensor:
	IRsensorValue = analogRead(IRsensorPin);	
	//output the value for IR sensor
	Serial.println("IR: " + IRsensorValue);
	
	// read the value from the US ECHO pin:
	USsensorValue = digitalRead(USsensorECHOPin);
	//output the value for US sensor
	Serial.println("US: " + USsensorValue);
	
	
	// read the value from button1:
	button1State = digitalRead(button1Pin);
	//output the value for button1 if pressed
	if (button1State == LOW){
		Serial.println("Button 1 Pressed");
	}
	
	// read the value from button2:
	button2State = digitalRead(button2Pin);
	//output the value for button2 if pressed
	if (button2State == LOW){
		Serial.println("Button 2 Pressed");
	}
	
	// read the value from button3:
	button3State = digitalRead(button3Pin);
	//output the value for button1 if pressed
	if (button3State == LOW){
		Serial.println("Button 3 Pressed");
	}
	//output speaker
	tone(speakerPin, 100, 100);
	
	motor.speed(rightMotor, 90);
	motor.speed(leftMotor, 90);
	
	delay(1000);
}