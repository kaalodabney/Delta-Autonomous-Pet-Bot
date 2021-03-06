#include "MotorDriver.h"
MotorDriver motor;

//declare analog pins
int IRsensorPin = A0;      // select the input pin for the IR sensor
//declare digital pins
int USsensorTRIGPin = 7;  // select the input pin for the US TRIG pin
int USsensorECHOPin = 6;  // select the input pin for the US ECHO pin
int button1Pin = 5;     // select the input pin for button 1
int button2Pin = 4;     // select the input pin for button 2
int button3Pin = 3;     // select the input pin for button 3
int speakerPin = 2;     // select the input pin for the speaker
//declare motor pins
int leftMotor = 1;
int rightMotor = 0;

//initialize input pins
int IRsensorValue = 0;
int USsensorValue = 0;
int button1State = HIGH;
int button1PrevState = HIGH;
int button2State = HIGH;
int button2PrevState = HIGH;
int button3State = HIGH;
int button3PrevState = HIGH;

void setup() {
  // set the pins
  pinMode(IRsensorPin, INPUT);
  pinMode(USsensorTRIGPin, OUTPUT);
  pinMode(USsensorECHOPin, INPUT);
  pinMode(button1Pin, INPUT_PULLUP);
  pinMode(button2Pin, INPUT_PULLUP);
  pinMode(button3Pin, INPUT_PULLUP);
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
  button1PrevState = button1State;
  button1State = digitalRead(button1Pin);
  //output the value for button1 if pressed
  if ((button1State == LOW) && (button1PrevState == HIGH)){
    Serial.println("Button 1 Pressed");
  }
  
  // read the value from button2:
  button2PrevState = button2State;
  button2State = digitalRead(button2Pin);
  //output the value for button2 if pressed
  if ((button2State == LOW) && (button2PrevState == HIGH)){
    Serial.println("Button 2 Pressed");
  }
  
  // read the value from button3:
  button3PrevState = button3State;
  button3State = digitalRead(button3Pin);
  //output the value for button1 if pressed
  if ((button3State == LOW) && (button3PrevState == HIGH)){
    Serial.println("Button 3 Pressed");
  }
  //output speaker
  tone(speakerPin, 100, 100);
  
  motor.speed(rightMotor, 90);
  motor.speed(leftMotor, 90);
  
  delay(1000);
}

void readDataIn(){
  int ex = 33;
  Serial.readBytesUntil(33, inBytes, 20);
  int i = 0;
  for(int x = 0; x < 20; x++){
    if(inBytes[x] != '/')
      dataIn[i] = dataIn[i] * 10 + inBytes[x] - '0';
    else{
      i++;
      if(i > 2)
        break;
    }
  }
  
}

void sendDataOut(int fed, int pat, int stats, int motorState, int us, int ir){
  String dataOut = String(fed) + '/' + String(pat) + '/' + String(stats) + '/' + String(motorState) + '/' + String(us) + '/' + String(ir) + '/';
  Serial.println(dataOut);
}
