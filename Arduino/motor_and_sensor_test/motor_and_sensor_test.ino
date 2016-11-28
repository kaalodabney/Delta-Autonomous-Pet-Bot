int analogPin = 0;


#include "MotorDriver.h"
MotorDriver motor;

#define trigPin 7
#define echoPin 6

void setup() {
  Serial.begin (9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  motor.begin();
}

void loop() {

  long duration, distance;
  digitalWrite(trigPin, LOW);  // Added this line
  delayMicroseconds(2); // Added this line
  digitalWrite(trigPin, HIGH);
//  delayMicroseconds(1000); - Removed this line
  delayMicroseconds(100); // Added this line
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = (duration/2) / 29.1;
  if (distance < 4) {  // This is where the LED On/Off happens
}

  if (distance >= 200){
    Serial.println(">= 200");
    motor.stop(0);
    motor.stop(1);
    
  } else if(distance <= 0) {
    Serial.println("<= 0");
  }
  else {
    Serial.print(distance);
    Serial.println(" cm");
  }
  if(distance <= 10){
    motor.speed(0, 95);
    motor.speed(1, -95);// set motor0 to speed 100
    delay(1000);
    Serial.println("stopping");
    motor.stop(1);
    motor.stop(0);
    //delay(1000);
  }
    
}
