#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 00:49:02 2025

@author: lubuntu
"""

#%%

import numpy as np
import matplotlib.pyplot as pl

def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)
    
def taylor4(x):
    """implements exp(-2*x-1) by 4th order taylor series"""
    return (    1-2*(x+0.5)
                 +2*(x+0.5)**2
                 -8./6.*(x+0.5)**3 
                 +16./24.*(x+0.5)**4 
            )

def taylorN(x,N=4):
    y=np.zeros_like(x)
    for n in range(N+1):
        y+=(-2)**n/factorial(n)*(x+0.5)**n
    return y

def taylorNnew(x,N=4):
    y=np.zeros_like(x)
    for i in range(len(y)):
        for n in range(N+1):
            y[i]+=(-2)**n/factorial(n)*(x[i]+0.5)**n
    return y

def taylorNnew(x, N = 4):
    y = np.zeros_like(x)
    for i in range(len(y)):
        for n in range(N+1):
            y[i] += (-2) ** n / factorial(n) * (x[i] + 0.5) ** n
    return y


#%%

N = 4
x = np.linspace(-1, 4, 21)
y = taylor4(x)
#yN = taylorN(x, N = 4)
yNnew = taylorNnew(x, N)
yN = taylorN(x, N)
yR = np.exp(-2 * x - 1)

#%%

abs_error = yN[-1] - yR[-1]
print('N = %i abs.error = %1.3e' % (N, abs_error))






#%%

pl.plot(x,y)
pl.plot(x,yN)
pl.plot(x,yR)
pl.plot(x,yNnew)

#pl.xlim([-2.5,3.5])
#pl.ylim([0,70])

pl.show()