# -*- coding: utf-8 -*-
import pandas as pd

import sympy as sp

import plotly.express as px

import random as rand

import matplotlib.pyplot as plt

import plotly.io as pio

pio.renderers.default = 'browser'

Heads = 'Heads'

Tails = 'Tails'

Coin = [Heads, Tails]

data = []

CountHeads = 0

for i in range(5000):
    temp = rand.choice(Coin)
    
    if temp == Heads:
        CountHeads = CountHeads + 1
    else:
        data.insert(i, CountHeads)
        CountHeads = 0

data = pd.DataFrame(data, columns = ['Flips'])
        
fig = px.histogram(data, x = 'Flips')

fig.show()


