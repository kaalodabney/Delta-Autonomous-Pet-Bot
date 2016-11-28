import time
import serial
import comsManagerAlpha
import ledManager

led = ledManager.LedManager()
coms = comsManagerAlpha.ComsManager()

coms.clearBufferOut()
coms.clearBufferIn()

coms.sendSerialData(13,222,1)
print("--------")
coms.waitUntilDataIn()
coms.receiveSerialData()    
    
dataList = coms.getData()
print("1:" + str(dataList[0]) + " 2:" + str(dataList[1]) + " 3:" + str(dataList[2]) + " 4:" + str(dataList[3]) + " 5:" + str(dataList[4]) + " 6:" + str(dataList[5]))
led.test()

coms.close()    
    
