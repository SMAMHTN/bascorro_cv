# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 17:10:17 2019

@author: Binatang Kesusahan
"""


def write(value, file_name):
    value = str(value)
    filename = file_name
    file = open(str(filename), "w")
    file.write(value)
    file.close()


def read(file):
    f = open(file, "r")
    return f.read()


def odd(param):
    param = int(param)
    if param % 2 == 0:
        return  param + 1
    else:
        return param