# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 23:18:44 2019

@author: Binatang Kesusahan
"""

def read(file):
    f = open(file, "r")
    return f.read()  

def saveConfig(value, file_name):
    value = str(value)
    filename = file_name + ".txt"
    file = open(str(filename), "w")
    file.write(value)
    file.close()
