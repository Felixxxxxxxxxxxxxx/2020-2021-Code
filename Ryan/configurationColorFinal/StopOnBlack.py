#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.



# Create your objects here.
ev3 = EV3Brick()

#Initialize Motors
cMotor = Motor(Port.C)
dMotor = Motor(Port.D)
robot = DriveBase(cMotor, dMotor, 56, 60)

#initialize color sensors
p1FSensor = ColorSensor(Port.S1)
p2BSensor = ColorSensor(Port.S2)
p3SSensor = ColorSensor(Port.S3)
frontColorSensorWhite = -1
backColorSensorWhite = -1
sideColorSensorWhite = -1
frontColorSensorBlack = -1
backColorSensorBlack = -1
sideColorSensorBlack = -1

# Write your program here.
def readAllValues():
    # Read all Files
    f = open("ConfiguredColor.txt", "r")
    global frontColorSensorWhite
    global backColorSensorWhite
    global sideColorSensorWhite
    global frontColorSensorBlack
    global backColorSensorBlack
    global sideColorSensorBlack
    frontColorSensorWhite = int(f.readline())
    backColorSensorWhite = int(f.readline())
    sideColorSensorWhite = int(f.readline())
    frontColorSensorBlack = int(f.readline())
    backColorSensorBlack = int(f.readline())
    sideColorSensorBlack = int(f.readline())
    print("In read all values" + str(frontColorSensorBlack))
    f.close()

def test():
    readAllValues()
    print("in test" + str(frontColorSensorBlack))

def stopOnWhiteF():
    
    readAllValues()
    print("Read configured color front value: " + str(frontColorSensorWhite))

    while p1FSensor.reflection() < frontColorSensorWhite:
        #print(frontColorSensorWhite)
        robot.drive(100,0)
    robot.stop(Stop.BRAKE)

def stopOnWhiteB():

    readAllValues()
    print("Read configured color back value: " + str(backColorSensorWhite))

    while p2BSensor.reflection() < backColorSensorWhite:
        print(backColorSensorWhite)
        robot.drive(-100,0)
    robot.stop(Stop.BRAKE)

def stopOnWhiteS():

    readAllValues()
    print("Read configured color side value: " + str(sideColorSensorWhite))

    while p3SSensor.reflection() < sideColorSensorWhite:
        print(sideColorSensorWhite)
        robot.drive(100,0)
    robot.stop(Stop.BRAKE)

def stopOnBlackF():
    
    readAllValues()
    print("Read configured color front value: " + str(frontColorSensorBlack))

    while p1FSensor.reflection() > frontColorSensorBlack:
        #print(frontColorSensorBlack)
        robot.drive(100,0)
    robot.stop(Stop.BRAKE)

def stopOnBlackB():

    readAllValues()
    print("Read configured color back value: " + str(backColorSensorBlack))

    while p2BSensor.reflection() > backColorSensorBlack:
        print(backColorSensorBlack)
        robot.drive(-100,0)
    robot.stop(Stop.BRAKE)

def stopOnBlackS():

    readAllValues()
    print("Read configured color side value: " + str(sideColorSensorBlack))

    while p3SSensor.reflection() > sideColorSensorBlack:
        print(sideColorSensorBlack)
        robot.drive(100,0)
    robot.stop(Stop.BRAKE)