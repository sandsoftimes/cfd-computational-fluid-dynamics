#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 04:16:32 2025

@author: lubuntu
"""

import numpy as np 
import numpy.random as rd
import matplotlib.pyplot as pl 

#%%

x = rd.rand(20)
print(x)

pl.figure(1)
pl.plot(x, 'o')

pl.xlabel('index i of array elements')
pl.ylabel('random number x[i]')
pl.title('plot of rd.rand()')

#%%

print('rd.rand(20) function values are, \n', x)

#%%

#u = rd.uniform(-3., 5., 20)
u = (5.-(-3.))*x + (-3.) # alternative

print(u)

pl.figure(2)
pl.plot(u, 'o')

pl.xlabel('index i of the array elements')
pl.ylabel('random value u[i]')
pl.title('plot of rd.uniform()')

#%%

bins = np.linspace(-3., 5., 40)

pl.figure(3)
pl.xlabel('bins')
pl.ylabel('counts per bin')
pl.hist(u, bins=bins)