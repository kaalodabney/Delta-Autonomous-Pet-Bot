import time
import serial
import ledManager

LedManager = ledManager.LedManager()
#mm
def main():
    #arduino = init()
    while 1:
        LedManager.update()

def init():
    LedManager = LedManager()
    
    arduino = serial.Serial('arduino port', 9600)
    sleep(1)
    arduino.write("test1")
    while arduino.in_waiting <= 0:
        pass
    test = arduino.readline()

    if test == "test2":
        ledManager.test()
    else:
        ledManager.flash()

    return arduino

main()
