String inputString;
bool stringComplete;
bool test;

void setup() {
  Serial.begin(9600);
  inputString.reserve(200);
  stringComplete = false;
  test = false;
}

void loop() {
  //checkSerialIn(stringComplete);
  if(Serial.available()){
    inputString = Serial.readString();
    if(inputString.equals("test1"){
      
    }
    Serial.println("test2");
  }
}



void checkSerialIn(bool stringComplete){
   if(stringComplete){
    if(inputString.equals("test1")){
      test = true;
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
*/
