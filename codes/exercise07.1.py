#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 00:44:39 2025

@author: lubuntu
"""

import numpy as np
import matplotlib.pyplot as pl

# load array data
path = '/home/lubuntu/' 
tValues = np.load(path+'tValues.npy') 
xValues = np.load(path+'xValues.npy')
yValues = np.load(path+'yValues.npy')
zValues = np.load(path+'zValues.npy')

# verify data by plot
#pl.plot(xValues, yValues, 'r-')

# verify data by checksum
checksum = xValues.sum()
print(f'{checksum=}')

# basic stats
def mean(data1d):
    mean = 0. 
    for i in range(len(data1d)):
        mean += data1d[i]
    mean /= len(data1d)
    return mean 

def variance_unbiased(data1d):
    mean1d1 = mean(data1d)
    variance = 0. 
    for i in range(len(data1d)):
        variance += (data1d[i] - mean1d1)**2
    variance /= (len(data1d) - 1)
    return variance 

def variance_biased(data1d):
    mean1d1  = mean(data1d)    # 1st moment 
    mean1d2  = mean(data1d**2) # 2nd moment 
    variance = mean1d2 - mean1d1**2
    return variance

#%%

# compute stats for given data
meanX = mean(xValues)
meanY = mean(yValues)

meanXref = np.mean(xValues)
meanYref = np.mean(yValues) 

pl.plot(meanX   , meanY   , 'ko', ms=10)
pl.plot(meanXref, meanYref, 'c*', ms=10)

print(f'{meanX=}')
print(f'{meanXref=}')

varXu = variance_unbiased(xValues)
varXb = variance_biased(xValues)
varXr = np.var(xValues)

print(f'{varXu=}')
print(f'{varXb=}')
print(f'{varXr=}')

varYu = variance_unbiased(yValues) 
varYb = variance_biased(yValues)
varYr = np.var(yValues)

stddevX = np.sqrt(varXr)
stddevY = np.sqrt(varYr)

pl.plot(xValues, yValues, 'r')

pl.axhline(meanY        , color='k', ls='--')
pl.axhline(meanY+stddevY, color='k', ls=':')
pl.axhline(meanY-stddevY, color='k', ls=':')

pl.axvline(meanX        , color='k', ls='--')
pl.axvline(meanX+stddevX, color='k', ls=':')
pl.axvline(meanX-stddevX, color='k', ls=':')

#%%

# histograms and PDF
pl.figure(1)
pl.plot(xValues, tValues, 'b-')
pl.xlabel('x')
pl.ylabel('t')

pl.figure(2)
pl.hist(xValues, bins=20, density=True)
pl.hist(xValues, bins=200, density=True)
pl.hist(xValues, bins=2000, density=True)
pl.xlabel('x')
pl.ylabel('probability density function (PDF)')

#%%

pl.figure(3)
pl.plot(xValues, yValues, 'b-')

#pl.figure(4)
#pl.hist2d(int(x), int(y), bins=40)

#%%

from whist2d import Whist2d

whist2d = Whist2d(xValues, yValues, bins=40)
whist2d.plot()
pl.show()