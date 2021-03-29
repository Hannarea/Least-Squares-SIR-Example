# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 15:11:33 2021

@author: hreed
"""

import numpy as np

def readData(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        data_str = lines[0]
        data = np.array([float(i) for i in data_str.split(',')])
    return data
