import serial
import time

class ComsManager:
	arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
	time.sleep(2)
	serialData = 0
	inBytes = bytes(0)
	dataIn = [0,0,0,0,0,0]

	def receiveSerialData(self):
		self.serialData = 0
		inBytes = self.arduino.readline()
		print(str(inBytes)) #test
		i = 0
		for x in range(0,len(inBytes)):
			print('x'+ str(inBytes[x]))
			if inBytes[x] != 47:
				self.dataIn[i] = self.dataIn[i] * 10 + int(inBytes[x]) - ord('0')
			else:
				i += 1
				print('i'+ str(i))
				if i > 5:
					print("break")
					break
			x += 1

 
	def sendSerialData(self, motorL, motorR, sound):
		dataOut = str(motorL) + '/' + str(motorR) + '/' + str(sound) + '/!'  #maybe error here
		print("sending:  " + str(bytes(dataOut, encoding='utf-8')))
		self.arduino.write(bytes(dataOut, encoding='utf-8'))

	def close(self):
		self.arduino.close()
	
	def getData(self):
		return self.dataIn

	def clearBufferIn(self):
		self.arduino.flushInput()
	
	def clearBufferOut(self):
		self.arduino.flushOutput()

	def waitUntilDataIn(self):
		while self.arduino.inWaiting() <= 0:
			pass
