#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 14:32:58 2025

@author: lubuntu
"""

import numpy as np
import matplotlib.pyplot as pl

def gauss(x, mu=0.3, sigma=1.2):
    return np.exp(-(x-mu)**2 / (2*sigma**2)) / np.sqrt(2*np.pi*sigma**2)

def gaussDeriv1(x, mu=0.3, sigma=1.2):
    return -(x-mu) / sigma**2 * gauss(x, mu, sigma)

def forwardDiff(x, y):
    z = np.zeros_like(x)
    for i in range(1, len(x), 1):
        z[i] = (y[i+1]-y[i]) / (x[i+1] - x[i])
        return z

def centralDiff(x, y):
    z = np.zeros_like(x)
    for i in range(0, len(x)-1, 1):
        z[i] = (y[i+1]-y[i-1]) / (x[i+1]-x[i-1])
    return z

def centralDiff_2ndDeriv(x, y):
    z = np.zeros_like(x)
    for i in range(0, len(x)-1, 1):
        z[i] = (y[i+1]-2*y[i]+y[i-1]) / ((x[i+1]-x[i-1])*0.5)**2
    return z

#generate 1-D grid
x = np.linspace(-5, 5, 1001)
#x = np.linspace(-5, 5, 11)

#compute function values
y = gauss(x)

#compute 1st deriv analytically
y_deriv1 = gaussDeriv1(x)

#compute 1st deriv numerically
y_fdm1 = forwardDiff(x, y)
y_cdm1 = centralDiff(x, y)

#compute 2nd derivative
y_fdm2 = forwardDiff(x, y_fdm1)
y_cdm2 = centralDiff_2ndDeriv(x, y)

#plot
pl.plot(x, y, 'k-', label='gauss curve')
pl.plot(x, y_deriv1, 'k--', label='first deriv.')

pl.plot(x, y_fdm1, 'r+:', label='forward FDM first deriv.')
pl.plot(x, y_cdm1, 'b.:', label='central FDM first deriv.')

pl.plot(x, y_fdm2, 'g-', label='forward FDM first deriv. twice')
pl.plot(x, y_cdm2, 'g+', label='central FDM second deriv.')

pl.xlabel('x')
pl.ylabel('y')

pl.grid()
pl.legend()