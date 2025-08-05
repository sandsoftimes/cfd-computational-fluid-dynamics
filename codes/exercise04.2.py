#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 15:20:28 2025

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

def getError(yNum, yRef):
    return np.abs(yNum, yRef)

#generate 1-D grid
x = np.linspace(-5, 5, 1003)
#x = np.linspace(-5, 5, 11)

dx = x[2]-x[1]
#print('dx: ', dx)

#print('first difference is: ', x[2]-x[1])
#print('second difference is: ', x[3]-x[2])

xwithGhostPts = np.linspace(-5.-dx, 5.+dx, 1003)
x = xwithGhostPts

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

#compute errors
err_fdm1 = getError(y_fdm1, y_deriv1)
err_cdm1 = getError(y_cdm1, y_deriv1)

err_fdm2 = getError(y_fdm2, y_cdm2)
#err_cdm2 = getError(y_cdm2, y_deriv2)

#plot

pl.figure(1)

pl.plot(x[1:1002], y[1:1002], 'k-', label='gauss curve')
pl.plot(x[1:1002], y_deriv1[1:1002], 'k--', label='first deriv.')

pl.plot(x[1:1002], y_fdm1[1:1002], 'r+:', label='forward FDM first deriv.')
pl.plot(x[1:1002], y_cdm1[1:1002], 'b.:', label='central FDM first deriv.')

pl.plot(x[1:1002], y_fdm2[1:1002], 'g-', label='forward FDM first deriv. twice')
pl.plot(x[1:1002], y_cdm2[1:1002], 'g+', label='central FDM second deriv.')

pl.xlabel('x')
pl.ylabel('y')

pl.grid()
pl.legend()

#------error--plotting

pl.figure(2)

pl.plot(x, err_fdm1, 'r+:', label='forward FDM first deriv.')
pl.plot(x, err_cdm1, 'b.:', label='central FDM first deriv.')

pl.plot(x, err_fdm2, 'g-', label='forward FDM first deriv. twice')

pl.yscale('log')

pl.axhline(10**-3, linewidth=3, color='k')

pl.xlabel('x')
pl.ylabel('abs.error')

pl.grid()
pl.legend()
pl.show()
