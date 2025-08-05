# -*- coding: utf-8 -*-
"""
Created on Wed Jul 30 05:42:49 2025

@author: faral
"""

import numpy as np
N=100
d=2.0e-4

GaussSum=0.5*d*N*(N+1)
print('GuassSum= ',np.around(GuassSum,decimals=2))

MySum=0.0
for n in range(N+1):
	MySum+=n*d
print('MySum= ',np.around(MySum,decimals=2))

#%%

def summation(N):
	MySum=0.0
	for n in range(N+1):
	MySum+=n*d
#%%

def summation(values):
	N=len(values)
	MySum=0.0
	for n in range(N+1):
		MySum+=values[n]
	return MySum