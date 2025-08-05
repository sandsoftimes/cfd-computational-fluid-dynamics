#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 25 17:50:52 2025

@author: lubuntu
"""

# modules
import numpy as np
import matplotlib.pyplot as pl

# function definitions
def f(x):
    return 1./(1.+x)

def lowerSum(a, b, N):
    # TODO: implement summation algorithm for quadrature rule
    h = (b-a) / N
    I = 0. 
    for i in range(N):
        xi = a + h*i   # nodal point coordinate
        I += f(xi) * h # nodal value 
    return I

def trapezoidalRule(a, b, N):
    h = (b-a)/N
    I = 0.
    for i in range(N):
        xi = a + h*i                  # nodal point coordinate left
        xip = xi + h                  # nodal point coordinate right
        I += (f(xi) + f(xip)) * h*0.5 # nodal value left + right
    return I


# maîn program
h = 1.e-4 # h = 1.e-2 or h = 1.e-6 etc
N = int((0.+1.) / h + 0.5)
print('N = ', N)
print('analyticValue = ', np.log(2.))
print('lowerSum = ', lowerSum(0., 1., N))
print('trapezoidalRule = ', trapezoidalRule(0., 1., N))

# visualization: compute the integral I numerically for multiple h then plot

listOfStepSizes = []
listOfLowerSumValues = []
listOfLowerSumErrors = []

listOfTrapezoidalValues = []
listOfTrapezoidalErrors = []

for h in [1.e-1, 1.e-2, 1.e-3, 1.e-4, 1.e-5, 1.e-6, 1.e-7]:
    N = int((0.+1.)/h + 0.5)
    Ilower = lowerSum(0., 1., N)
    Itrapezoidal = trapezoidalRule(0., 1., N)
          
    listOfStepSizes.append(h)
    listOfLowerSumValues.append(Ilower)
    listOfLowerSumErrors.append(Ilower - np.log(2.))
          
    listOfTrapezoidalValues.append(Itrapezoidal)
    listOfTrapezoidalErrors.append(np.abs(Itrapezoidal - np.log(2.)))
          
#pl.plot(listOfStepSizes, listOfLowerSumValues, 'bo')
pl.loglog(listOfStepSizes, listOfLowerSumErrors, 'rs:')
pl.loglog(listOfStepSizes, listOfTrapezoidalErrors, 'g^:')

pl.xlabel('step size $h$')
#pl.ylabel('integral $I_h$')
pl.ylabel('error $varepsilon_h$')

pl.grid()
pl.show()