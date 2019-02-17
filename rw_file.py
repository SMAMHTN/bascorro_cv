# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 17:10:17 2019

@author: Binatang Kesusahan
"""
def write(text):
    text = str(text)
    file = open("file.txt", "w")
    file.write(text)
    file.close()

def read(file):
    f = open(file)
    return f.readlines()
    
    

write(12)

#f = open("setting/LH.txt")
#print(f.readline())
# 