#include "MotorDriver.h"
MotorDriver motor;

// === START ====== sound public varibles ======/
#define soundPin 2

int songTone[7][8] = { { 404 }, 
            { 780, 700, 780, 700 }, 
            { 700, 510, 690 }, 
            { 500, 600, 500, 600 }, 
            { 300, 450, 600 }, 
            { 400, 400, 300 }, 
            { 330, 550 }
          };
int songTone_Length[7] = { 1, 6, 3, 4, 3, 3, 2 };
double songTone_Time[7][8] = { { 1 }, 
                { 0.5, 0.5, 0.5, 0.5, 0.5, 0.5 }, 
                { 1.5, 0.5, 1 }, 
                { 0.25, 0.25, 0.25, 0.25 }, 
                { 1, 0.5, 1.5 }, 
                { 0.5, 0.5, 0.5 }, 
                { 0.5, 0.5 } 
              };

int tone_StartTime = 0;
int soundIndex_Playing = -1;
int toneIndex_Playing = 0;
// === E N D ====== sound public varibles ======

//declare analog pins
int IRsensorPin = A0;      // select the input pin for the IR sensor
//declare digital pins
int USsensorTRIGPin = 6;  // select the input pin for the US TRIG pin
int USsensorECHOPin = 7;  // select the input pin for the US ECHO pin
int button1Pin = 3;     // select the input pin for button 1
int button2Pin = 4;     // select the input pin for button 2
int button3Pin = 5;     // select the input pin for button 3
int speakerPin = 2;     // select the input pin for the speaker
//declare motor id
int leftMotor = 1;
int rightMotor = 0;

//declare vars for serial coms
char inBytes[20]; // buffer for bytes coming into serial
int dataOut[6];   // array to store data going to RPI [0] = fed button pressed, [1] = pat button pressed, [2] = show stats button pressed, [3] = motorState(1=on/0=off), [4] = ultra sonic sensor value, [5] = ir sensor value 
int dataIn[3];    // array to store data coming in from RPI [0] = motorL, [1] = motorR, [2] = sound

//initialize input pins
int IRsensorValue = 0;
int USsensorValue = 0;
int button1State;
int button1PrevState;
int button2State;
int button2PrevState;
int button3State;
int button3PrevState = HIGH;

void setup() {
  // set the pins
  pinMode(IRsensorPin, INPUT);
  pinMode(USsensorTRIGPin, OUTPUT);
  digitalWrite(USsensorTRIGPin, LOW);
  //pinMode(USsensorECHOPin, INPUT);
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
  while(Serial.available() <= 0){
    ;
  }
}

void loop() {
  while(Serial.available() <= 0){
    ;
  }
  readDataIn();

  setMotors(dataIn[0], dataIn[1]);

  /*
  sound index list
  const int s_error = 0;
  const int s_petting = 1;
  const int s_feed = 2;
  const int s_hungry = 3;
  const int s_hello = 4;
  const int s_goodbye = 5;
  const int s_hitwall = 6;
  */
  PlaySound(dataIn[2], true);
  PlayTone();
  
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
  dataOut[5] = digitalRead(IRsensorPin);  
  
  sendDataOut(dataOut[0], dataOut[1], dataOut[2], dataOut[3], dataOut[4], dataOut[5]);
}

void setMotors(int motorL, int motorR){
  motorL = motorL * -1;
  motorR = motorR * -1;
  if(motorL == 0){
      motor.brake(leftMotor);
      dataOut[3] = 0;
  } else {
      motor.speed(leftMotor, motorL);
      dataOut[3] = 1;
  }

  if(motorR == 0){
      motor.brake(rightMotor);
      dataOut[3] = 0;
  } else {
      motor.speed(rightMotor, motorR);
      dataOut[3] = 1;
  }  
}

//gets distance from the ultra sonic sensor
long getDistance() {
  long duration;
  unsigned int distanceCm;
  digitalWrite(USsensorTRIGPin, LOW);  // Added this line 
  delayMicroseconds(5); // Added this line
  digitalWrite(USsensorTRIGPin, HIGH);
  delayMicroseconds(10); // Added this line
  digitalWrite(USsensorTRIGPin, LOW);
  pinMode(USsensorECHOPin, INPUT);
  duration = pulseIn(USsensorECHOPin, HIGH);
  distanceCm = int((duration / 2) / 29.1);
  if (distanceCm >= 200){
    //distanceCm = 200;
  } else if (distanceCm <= 0){
    distanceCm = 0;
  }
  return distanceCm;
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
  Serial.flush();
}


void PlayTone() {
  if (soundIndex_Playing < 0)
    //NOT playing
    return;

  if (tone_StartTime == 0) {
    tone_StartTime = millis();
    tone(soundPin, songTone[soundIndex_Playing][toneIndex_Playing]);
  } else if (millis() - tone_StartTime >= songTone_Time[soundIndex_Playing][toneIndex_Playing]) {
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
