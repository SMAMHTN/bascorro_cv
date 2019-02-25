# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 21:40:03 2019

@author: Binatang Kesusahan
"""
import sys
from serial import Serial

def main():
    ser = Serial('COM3',)
    ser.baudrate = 115200

    while 1:
        var = input("input somethin : ")
        
        if (var == '1'):
            ser.write(str(1).encode())
            print('led should on now')
        
        if (var == '0'):
            ser.write(str(0).encode())
            print('led should off now')    
        
    print(ser.readline())
    return 0

main()