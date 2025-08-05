#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 04:31:49 2025

@author: lubuntu
"""

import numpy as np
import numpy.random as rd
import matplotlib.pyplot as pl 

dice = rd.randint(1, 7, 5000)

pl.figure(1)
pl.xlabel('dice roll number i')
pl.ylabel('dice result')
pl.plot(dice, 'o')

bins = np.linspace(0.5, 6.5, 7)

pl.figure(2)
pl.xlabel('dice results (bins)')
pl.ylabel('probability density')
pl.hist(dice, bins=bins, density=True)

p = 1. / 6. 
pl.axhline(p, color='k', ls='--')

mean = np.mean(dice)
stddev = np.std(dice)
print('mean stddev =', mean, stddev)