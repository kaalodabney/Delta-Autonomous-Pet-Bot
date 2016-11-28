char inBytes[20];
int err;
//values send to RPI [0] = fed, [1] = pat, [2] = stats, [3] = motorState, [4] = us, [5] = ir; 
int dataOut[6];
//values taken in from RPI [0] = motorL, [1] = motorR, [2] = sound (ascii code)
int dataIn[3];
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
  for(int i = 0; i < 6; i++){
    dataOut[i] = i;
  }
  while(!Serial){
  }
}

void loop() {
  while(Serial.available() <= 0){
    digitalWrite(LED_BUILTIN, LOW);//wait until serial data available
  }
  
  readDataIn();
  if(dataIn[0] == 13){
    digitalWrite(LED_BUILTIN, HIGH);
    delay(1000);
    digitalWrite(LED_BUILTIN, LOW);
  }
  Serial.flush();
  sendDataOut(dataIn[0], dataIn[1], dataIn[2], dataOut[3], dataOut[4], dataOut[5]);
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

/*void getSerial() {
  serialData = 0;
  while (inByte != '/') {
    inByte = Serial.read();
    if(inByte > 0 && inByte != '/') {
      serialData = serialData * 10 + int(inByte);
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
          a = serialData;
          break;
        }
      //data for right motor
      case 2:
        {
          getSerial();
          b = serialData;
          break;
        }
      //tune to play  
      case 3: 
        {
          getSerial();
          c = char(serialData);
          break;
        }
    }
  }
}

//called at end of loop to send data to the raspberry pi for the AI to determine what to do next loop
void sendDataOut(int a, int b, int c){ 
  int err;
  //char dataOut[50];
  //err = sprintf(dataOut, "1/%d/2/%d/3/%d/4/%d/5/%d/", a,b,c,c,c);
  //if(err < 0)
  //  Serial.write("0/");
  //else
    Serial.write("1/13/2/22/3/3/4/4/5/5/");
}*/
