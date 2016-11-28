import serial

class ComsManager:
    arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    serialData = 0
    inByte = bytes(0)
    dataList = [0, 1, 2, 3, 4]
    
    #reads a byte array from serial until the '/' character    
    def getSerial(self):
        print("---------")
        print("getSerial, inByte: " + str(self.inByte))              #test
        self.serialData = 0
        while self.inByte != bytes("/", encoding='utf-8'):
            self.inByte = bytes(self.arduino.readline())
            if (ord(self.inByte) == 47):                                 #test
                print('inByte     = ' + str(self.inByte))           #test 
            if (self.inByte > bytes(0)) & (ord(self.inByte) != ord('/')):
                print("serialData = " + str(self.serialData))        #test
                print("inByte     = " + str(self.inByte))           #test
                self.serialData = self.serialData * 10 + int(self.inByte)
        print("serialData =" + str(self.serialData))                                 #test  
        print("end getSerial")
        print("-------------")
        self.inByte = 0
        return self.serialData

    def receiveSerialData(self):
        while self.arduino.inWaiting() > 0:
            print("serial > 0, inWaiting: " + str(self.arduino.inWaiting()))
            self.getSerial()
            if self.serialData == 0:
                return 0
            #get fed    
            elif self.serialData == 1:
                print("one") 
                self.getSerial()
                print("serialData: "+ str(self.serialData))
                print("inWaiting: " + str(self.arduino.inWaiting()))
                self.dataList[0] = int(self.serialData)
                print("dataList[0]: " + str(self.dataList[0]))
            #get pat    
            elif self.serialData == 2: 
                self.getSerial()
                print("two")
                self.dataList[1] = self.serialData
            #get motorState
            elif self.serialData == 3:
                self.getSerial()
                print("three")
                self.dataList[2] = self.serialData                    
            #get ultra sonic data
            elif self.serialData == 4: 
                self.getSerial()
                print("four")
                self.dataList[3] = self.serialData
            #get ir data    
            elif self.serialData == 5:
                self.getSerial()
                print("five")
                self.dataList[4] = self.serialData

            return 1

    #sends data in byte array form from the rpi to the arduino, args: motorL and motorR are ints and sound is a char
    def sendSerialData(self, motorL, motorR, sound):
        dataOut = "1/" + str(motorL) + "/2/" + str(motorR) + "/3/" + sound + "/"
        print(dataOut)
        print(bytes(dataOut, encoding='utf-8'))
        self.arduino.write(bytes(dataOut, encoding='utf-8'))


    def close(self):
        self.arduino.close()

    def getData(self):
        return self.dataList

    def clearBufferIn(self):
        self.arduino.flushInput()

    def clearBufferOut(self):
        self.arduino.flushOutput()

    def waitUntilDataIn(self):
        while self.arduino.inWaiting() <= 0:
            pass
