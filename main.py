#!/usr/bin/env python3
from ev3dev2.motor import *
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds

#see https://python-ev3dev.readthedocs.io/en/ev3dev-stretch/motors.html
robot = MoveSteering(OUTPUT_B, OUTPUT_C)

robot.on_for_rotations(0,SpeedPercent(25),2, brake=True,block=True)