#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.hubs import EV3Brick
ev3 = EV3Brick()
cs = ColorSensor(Port.S1)
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
robot = DriveBase(left_motor, right_motor, wheel_diameter=62, axle_track=152.4)

refl = cs.reflection()
while cs.reflection() < (refl + 5):
    robot.drive(100 , 0)
    robot.stop
    Stop.BRAKE