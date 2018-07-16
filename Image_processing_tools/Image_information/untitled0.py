#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 16 18:41:37 2018

@author: wdh
"""
from PIL import Image
import os
import numpy as np
def look(dir):
    file_list = os.listdir(dir)
    print(file_list)
    for filename in file_list:
        path = ''
        path = dir+filename
        img = np.array(Image.open(path))
        print("1")

dir="/home/wdh/DataSets/hand-segmentation/From Cai/Resize/Masks/"
look(dir)