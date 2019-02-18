# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 17:10:17 2019

@author: Binatang Kesusahan
"""
def write(value, file_name):
    value = str(value)
    filename = value + ".txt"
    file = open(str(filename), "w")
    file.write(value)
    file.close()

def read(file):
    f = open(file, "r")
    return f.read()
    
    

write(90, file)

f = open("file.txt")
print(f.readline())
 