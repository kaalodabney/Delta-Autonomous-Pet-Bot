import serial
import time

class ComsManager:
    arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    time.sleep(2)
    inBytes = bytes(0)
    dataIn = [0,0,0,0,0,0]

    def receiveSerialData(self):
        serialData = 0
        inBytes = self.arduino.readline()
        print(str(inBytes)) #test
        i = 0
        for x in range(len(inBytes)):
            if inBytes[x] != 47:
                serialData = serialData * 10 + int(inBytes[x]) - ord('0')
            else:
                self.dataIn[i] = serialData
                i += 1
                serialData = 0
                if i >= 6:
                    break

    def sendSerialData(self, motorL, motorR, sound):
        dataOut = str(motorL) + '/' + str(motorR) + '/' + str(sound) + '/!'  #maybe error here
        print("sending:  " + str(bytes(dataOut, encoding='utf-8')))
        self.arduino.write(bytes(dataOut, encoding='utf-8'))

    def close(self):
        self.arduino.close()
	
    def getData(self):
        return self.dataIn

    def flush(self):
        self.arduino.flush()

    def clearBufferIn(self):
        self.arduino.flushInput()
	
    def clearBufferOut(self):
        self.arduino.flushOutput()

    def waitUntilDataIn(self):
        while self.arduino.inWaiting() <= 0:
            pass
