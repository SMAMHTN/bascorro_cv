# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 17:10:17 2019

@author: Binatang Kesusahan
"""


def write(value, file_name):
    """part of callback function when changing the trackbars in object detection configuration script

    Parameter
    ---------
    value : int
        value to write to the file
    file_name : string
        file to read, include the extension
    """
    value = str(value)
    filename = file_name
    file = open(str(filename), "w")
    file.write(value)
    file.close()


def read(file):
    """also part of callback function when changing the trackbars in object detection configuration script

    Parameters
    ---------
    file : str
        file to read, include the extension"""
    f = open(str(file), "r")
    return f.read()


def odd(param):
    """file for convert to odd number because all kernel size parameter only able to process with odd number

    Parameters
    ----------
    param : int
        usually variable with 'kernel' in its name

    Returns
    -------
    int
        odd integer number
    """
    param = int(param)

    if param % 2 == 0:
        return  param + 1
    else:
        return param
