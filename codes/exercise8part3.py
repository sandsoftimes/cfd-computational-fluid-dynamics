#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 05:15:08 2025

@author: lubuntu
"""

import numpy as np 
import numpy.random as rd 
import matplotlib.pyplot as pl

N = 5000

r = rd.exponential(size=5000)

pl.figure(1)
pl.xlabel('sample index')
pl.ylabel('random value')
pl.plot(r, 'o')

bins = np.linspace(0., 10., 101)

pl.figure(2)
pl.xlabel('bins')
pl.ylabel('probability density')
pl.hist(r, bins=bins, density=True, color='b')

#%%

u = rd.rand(5000)

n = -np.log(1. -u)

pl.hist(n, bins=bins, density=True, color='r')

#%%

x = np.linspace(0., 10., 200)
p = np.exp(-x)
pl.plot(x, p, 'k--')

pl.xlim([0., 10.])

pl.draw()