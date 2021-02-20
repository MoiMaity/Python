# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 21:55:41 2018

@author: shiba
"""
import random


values = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
suites = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

deck = [f'{val} of {suit}' for suit in suites for val in values]
random.shuffle(deck)
hands = [deck[0::4] for i in range(0, 4)] 
print (hands[0],'\n')


#deck = [ f'{color}-{num}']