# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 16:32:11 2022

@author: mbles
"""

import random as rand

import matplotlib.pyplot as plt

import plotly.express as ply

import pandas as pd

import plotly.io as pio

pio.renderers.default='browser'

Heads = 'Heads'

Tails = 'Tails'

Coin = [Heads, Tails]

data = []


def CoinFlip():

    CountHeads = 0
    
    CountTails = 0
    
    for i in range(5000):
        
        temp = rand.choice(Coin)
    
        if temp == Heads:
            CountHeads = CountHeads + 1
        else:
            CountTails = CountTails + 1
    
    return CountHeads / CountTails
        

for i in range(500):
    
    data.insert(i, CoinFlip())

data = pd.DataFrame(data, columns = ['Ratio'])

#fig = hist(data)

#fig.show()

fig = ply.histogram(data, x = "Ratio")

fig.show()


