import time
import serial
import ledManager
import comsManager
import hunger
import happy
import fatigue
import bond

coms = comsManager.ComsManager()
hunger = hunger.HungerManager()
happy = happy.HappyManager()
fatigue = fatigue.FatigueManager()
bond = bond.BondManager()
led = ledManager.LedManager()
sound = soundManager.SoundManager()
movement = movementManager.MovementManager()



# list of data sent from arduino
# data[0] = button 1 / fed
# data[1] = button 2 / pat
# data[2] = button 3 / show stats
# data[3] = motorState
# data[4] = ultra sonic sensor
# data[5] = ir sensor
def main():
    init()
    while 1:
        coms.receiveSerialData()
        dataIn = coms.getData()#list of data sent from arduino
        hunger.update(data[0], data[3])
        happy.update(hunger.getHungerMod(), data[1])
        fatigue.update(data[3])
        bond.update(happy.getHappyMod(), data[1], data[2])
        led.update(happy.getHappyLevel(), fatigue.getFatigue)
        sound.update(happy.getHappyLevel(), data[0], data[1], data[4], data[5])
        movement.update(data[0], data[1], data[4], data[5])
        coms.sendSerialData(movement.getMotor1(), movement.getMotor2(), sound.getTune())

def init():
    if coms.testComs():
        ledManager.test()
    else:
        ledManager.flash()

    
main()
