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

//declare vars for serial coms
char inBytes[20]; // buffer for bytes coming into serial
int dataOut[6];   // array to store data going to RPI [0] = fed button pressed, [1] = pat button pressed, [2] = show stats button pressed, [3] = motorState(1=on/0=off), [4] = ultra sonic sensor value, [5] = ir sensor value 
int dataIn[3];    // array to store data coming in from RPI [0] = motorL, [1] = motorR, [2] = sound

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
  motor.begin();

  
  //open serial port
  Serial.begin(9600);
  while(!Serial){
    ; // do nothing until serial connected
  }
}

void loop() {
  while(Serial.available() <= 0){
    ; // do nothing until serial data comes in
  }
  
  readDataIn();
  Serial.flush();  

  motor.speed(leftMotor, dataIn[0]);
  motor.speed(rightMotor, dataIn[1]);
  //TODO: sound stuff here with dataIn[2]
  
  // read the value from button1:
  button1PrevState = button1State;
  button1State = digitalRead(button1Pin);
  dataOut[0] = 0;
  //output the value for button1 if pressed
  if ((button1State == LOW) && (button1PrevState == HIGH)){
    dataOut[0] = 1;
  }
  
  // read the value from button2:
  button2PrevState = button2State;
  button2State = digitalRead(button2Pin);
  dataOut[1] = 0;
  //output the value for button2 if pressed
  if ((button2State == LOW) && (button2PrevState == HIGH)){
    dataOut[1] = 1;
  }
  
  // read the value from button3:
  button3PrevState = button3State;
  button3State = digitalRead(button3Pin);
  dataOut[2] = 0;
  //output the value for button1 if pressed
  if ((button3State == LOW) && (button3PrevState == HIGH)){
    dataOut[2] = 1;
  }

  if((dataIn[0] != 0) || (dataIn[1] != 0)){
    dataOut[3] = 1;
  } else {
    dataOut[3] = 0;
  }

  // read the value from the US ECHO pin:
  dataOut[4] = getDistance();
  // read the value from the IR sensor:
  dataOut[5] = analogRead(IRsensorPin);  
  
  Serial.flush();
  sendDataOut(dataIn[0], dataIn[1], dataIn[2], dataOut[3], dataOut[4], dataOut[5]);
}

//gets distance from the ultra sonic sensor
long getDistance() {
  long duration, Distance;
  digitalWrite(USsensorTRIGPin, LOW);  // Added this line 
  delayMicroseconds(2); // Added this line
  digitalWrite(USsensorTRIGPin, HIGH);
  delayMicroseconds(10); // Added this line
  digitalWrite(USsensorTRIGPin, LOW);
  duration = pulseIn(USsensorECHOPin, HIGH);
  Distance = (duration / 2) / 29.1;
  if (Distance >= 200 || Distance <= 0)
    return 200;
  return Distance;
}

//reads a string of data in from serial until '!' character
//stores data from string in array of ints
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
