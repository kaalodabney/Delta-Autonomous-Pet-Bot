import time
import serial
import ledManager
#import comsManager
import hungerManager
import happyManager
import fatigueManager
import bondManager
#import soundManager
import movementManager

#coms = comsManager.ComsManager()
hunger = hungerManager.HungerManager()
happy = happyManager.HappyManager()
fatigue = fatigueManager.FatigueManager()
bond = bondManager.BondManager()
led = ledManager.LedManager()
#sound = soundManager.SoundManager()
movement = movementManager.MovementManager()



# list of data sent from arduino
# data[0] = button 1 / fed
# data[1] = button 2 / pat
# data[2] = button 3 / show stats
# data[3] = motorState
# data[4] = ultra sonic sensor
# data[5] = ir sensor
def main():
    while 1:
#        coms.receiveSerialData()
#        dataIn = coms.getData()#list of data sent from arduino
        dataIn = [1, 0, 0, 0, 50, 50]
        hunger.update(dataIn[0], dataIn[3])
        happy.update(hunger.getHungerMod(), dataIn[1])
        fatigue.update(dataIn[3])
        bond.update(happy.getHappyMod(), dataIn[1], dataIn[0])
#        led.update(happy.getHappyLevel(), fatigue.getFatigue)
#        sound.update(happy.getHappyLevel(), data[0], data[1], data[4], data[5])
        movement.update(happy.getHappyLevel(), bond.getBondLevel(), fatigue.getFatigueLevel(), dataIn[4], dataIn[5], dataIn[0], dataIn[1])
#
#        coms.sendSerialData(movement.getMotor1(), movement.getMotor2(), sound.getTune())
   

   
main()
