import time
import serial
import comsManager
import ledManager

led = ledManager.LedManager()
coms = comsManager.ComsManager()
sleep(.5)
coms.sendSerialData(1,2,3)

if coms.receiveSerialData() == 0:
    print "error receiving data/n"
else:
    print "data received/n"
    dataList = coms.getData
    print '\n'.join(str(p) for p in dataList)
    led.test()
    
    
