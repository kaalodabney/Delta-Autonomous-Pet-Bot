import serial

class ComsManager:
    arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=5)
    inByte = 0
    dataList = [0, 1, 2, 3, 4]
    
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
                return 0
            #get fed    
            elif serialData == 1: 
                self.getSerial()
                self.dataList[0] = serialData
            #get pat    
            elif serialData == 2: 
                self.getSerial()
                self.dataList[1] = serialData
            #get motorState
            elif serialData == 3:
                self.getSerial()
                self.dataList[2] = serialData                    
            #get ultra sonic data
            elif serialData == 4: 
                self.getSerial()
                self.dataList[3] = serialData
            #get ir data    
            elif serialData == 5:
                self.getSerial()
                self.dataList[4] = serialData

            return 1

    #sends data in byte array form from the rpi to the arduino, args: motorL and motorR are ints and sound is a char
    def sendSerialData(self, motorL, motorR, sound):
        dataOut = "1/" + str(motorL) + "/2/" + str(motorR) + "/3/" + sound + "/"
        serial.write(bytes(dataOut, encoding='utf-8'))


    def getData(self):
        return dataList
