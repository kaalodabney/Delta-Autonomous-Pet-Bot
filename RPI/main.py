import time
import serial
import ledManager
import comsManager

led = ledManager.LedManager()

def main():
    init()
    while 1:
        led.update()

def init():
    led = ledManager.LedManager()

    coms = comsManager.ComsManager()
    if coms.testComs():
        ledManager.test()
    else:
        ledManager.flash()

    
main()
