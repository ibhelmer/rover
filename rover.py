# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 23:54:48 2018
Simpel demo for controlling rover.
The demo is using PWM output to the motors and is controlled with the following key:
a - decrease output to left motor by 10%
s - increasing output to left motor by 10 %
d - increasing output to right motor by 10 %
f - decreasing output to right motor by 10 %
b - break both output set to 0
w - output left and right set to 50%

@author: IHN
"""
# Import of lib
from gpiozero import LED
from gpiozero import PWMLED
from time import sleep
import sys, termios, tty, os

# Setup ports
mIn1 = LED(26)
mIn2 = LED(16)
mEn1 = PWMLED(12)
mIn3 = LED(20)
mIn4 = LED(21)
mEn2 = PWMLED(13)

# Global variables
left = 0.0
right = 0.0

# Function for reading keypress, return character value
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

# Function for controlling left motor
def leftmotor(lspeed):
    if lspeed < 0 :
        mIn1.on()
        mIn2.off()
        mEn1.value = abs(lspeed)
    else :
       	mIn1.off()
        mIn2.on()
        mEn1.value = lspeed

# Function for controlling right motor
def rightmotor(rspeed):
    if rspeed < 0 :
        mIn3.on()
        mIn4.off()
        mEn2.value = abs(rspeed)
    else :
        mIn3.off()
        mIn4.on()
        mEn2.value = rspeed

# Main super loop
while True:
    char = getch()  # Read keyboard	
    if char=='a':
        left=left-0.1
        leftmotor(left)
        print(left)
    if char=='s':
        left=left+0.1
        leftmotor(left)
        print(left)
    if char=='f':
        right=right-0.1
        rightmotor(right)
        print(right)
    if char=='d':
        right=right+0.1
        rightmotor(right)
        print(right)
    if char=='b':
        right = 0.0
        left = 0.0
        rightmotor(right)
        leftmotor(left)
    if char=='w':
        right = 0.5
        left = 0.5
        rightmotor(right)
        leftmotor(left)
