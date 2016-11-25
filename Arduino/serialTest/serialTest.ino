int inByte;
unsigned long serialData = 0;
int a, b, c, d, e;

void setup() {
  Serial.begin(9600);
  while(!Serial){
  }
}

void loop() {
  while(Serial.available() < 0){
    //wait untill serial data available
  }
  readDataIn();
  sendDataOut(a,b,c);
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
          a = serialData;
          break;
        }
      case 2:
        {
          getSerial();
          b = serialData;
          break;
        }
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
  char dataOut[50];
  err = sprintf(dataOut, "1/%d/2/%d/3/%d/4/%d/5/%d/", a,b,c,c,c);
  if(err < 0)
    Serial.write("0/");
  else
    Serial.write(dataOut);
}
