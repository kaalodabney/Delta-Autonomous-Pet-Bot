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
String inputString = "";
boolean stringComplete = false;


void setup() {
  Serial.begin(9600);
  inputString.reserve(200);
  
  pinMode(UltraS_trigPin, OUTPUT);
  pinMode(UltraS_echoPin, INPUT);

  pinMode(Motor_button, INPUT_PULLUP);
  buttonOn = false;
  motor.begin();

}

void loop() {
  checkSerialIn(stringComplete);
    
  if (digitalRead(Motor_button) == LOW){
    buttonOn = !buttonOn;
  }
    
  if (buttonOn) {
    if (GetDistance() < 50) {
      Stop();
    } else {
      Serial.println("motorOn");
      Move(500, 500);
    }
  } else {
    Stop();
  }
}

long GetDistance() {
  long duration, distanceCM;
  
  digitalWrite(UltraS_trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(UltraS_trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(UltraS_trigPin, LOW);
  duration = pulseIn(UltraS_echoPin, HIGH);
  
  distanceCM = microsecondsToCM(duration);
  if (distanceCM >= 200 || distanceCM <= 0)  //this checks if distance is outside of ultrasonic range, what for and why return 10240?
    return 10240;   
  return distanceCM;
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
  Serial.println("motorOff");
  Move(0);
}

long microsecondsToCM(long duration){
  return (duration / 2) / 29.1;
}

void checkSerialIn(bool stringComplete){
   if(stringComplete){
    if(inputString.equals("ledOn")){
      //led on
    }else if(inputString.equals("ledOff")){
      //led off
    }
    inputString = "";
    stringComplete = false;
  }
}


/*
  SerialEvent occurs whenever a new data comes in the
 hardware serial RX.  This routine is run between each
 time loop() runs, so using delay inside loop can delay
 response.  Multiple bytes of data may be available.
 */
void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag
    // so the main loop can do something about it:
    if (inChar == '\n') {
      stringComplete = true;
    }
  }
}



