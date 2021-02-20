# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 18:27:20 2018

@author: shiba
"""
import random

# =============================================================================
# colors = ['Light gray', 'Cyan', 'Black']
# # 8 walls
# sel_colors = random.choices(colors, weights = [40, 40, 20], k = 8)
# print(sel_colors)
# =============================================================================

my_list = list(range(100))
print(my_list)
print()
random.shuffle(my_list)
print(my_list)
print()
selected_vals = random.sample(my_list, k = 5)
print(selected_vals)








