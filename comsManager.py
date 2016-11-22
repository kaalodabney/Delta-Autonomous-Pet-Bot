import serial

class ComsManager:
    arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=5)

    #tests communications between arduino and rpi
    def testComs(self):
        sleep(.5) #to allow time for the serial to open
        arduino.println("test1")
        
        while arduino.in_waiting <= 0:
            pass
        
        test = arduino.readline
        if test == "test2":
            return true
        else:
            return false
                
        
