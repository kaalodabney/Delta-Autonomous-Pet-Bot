import serial

class ComsManager:
    arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=5)
    inByte = 0
    dataList #todo: create dataList
    
    #tests communications between arduino and rpi
    def testComs(self):
        #todo: test case

    #reads a byte array from serial until the '/' character    
    def getSerial(self):
        serialdata = 0
        inbyte = 0
        while inbyte != '/':
            inbyte = arduino.read()
            if inbyte > 0 && inbyte != '/':
                serialdata = serialdata * 10 + inbyte - '0'
        inByte = 0
        return serialData

    def receiveSerialData(self):
        while arduino.available() > 0:
            self.getSerial()
            if serialData == 0:
                #todo: handle error
            elif serialData == 1:
                #todo: finish handling data from arduino

    def sendSerialData(self, motorL, motorR, sound):
        #todo: parse and send serial data to arduino
