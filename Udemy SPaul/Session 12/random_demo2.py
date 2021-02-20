# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 16:22:07 2018

@author: shiba
"""

import random

first_name = ['Adrian', 'Austin', 'Diana', 'Emily', 'John']
last_name = ['Berry', 'Dickens', 'Howard', 'Langdon', 'Martin']

for i in range(10):    
    f_name = random.choice(first_name)
    l_name = random.choice(last_name)
    name = f_name + ' ' + l_name    
    contact = f'{random.randint(100,999)}-555-{random.randint(1000,9999)}'
    print(name, '\n', contact, end='\n')
    print()



