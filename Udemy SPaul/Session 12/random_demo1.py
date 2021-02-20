# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 12:04:40 2018

@author: shiba
"""

import random
min = 5.0
max = 12.0
width = max - min

for i in range(10):        
    #v = random.random() * width + min # >=0 < 1, [0,1)
    v = random.randint(min, max) #  >= min and <=max
    print(v)