#!/usr/bin/env python3
from ev3dev2.motor import *
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.wheel import Wheel
#see https://python-ev3dev.readthedocs.io/en/ev3dev-stretch/motors.html


class BaloonWheel(Wheel):
    def __init__(self):
        Wheel.__init__(self,56,28)

def inches_to_mm(inches):
    return inches * 25.4;

STUD_MM=8

robot = MoveDifferential(OUTPUT_B, OUTPUT_C, BaloonWheel, 14* STUD_MM)

SPEED=40

robot.on_for_distance(SpeedPercent(SPEED),inches_to_mm(12),brake=False,block=True)
robot.turn_right(SPEED,90,brake=True,block=True)
robot.on_for_distance(SpeedPercent(SPEED),inches_to_mm(24),brake=True,block=True)