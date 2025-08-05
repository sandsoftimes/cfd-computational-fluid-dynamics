#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 02:05:24 2025

@author: lubuntu
"""
import numpy as np
import matplotlib.pyplot as pl

#%%

matrixA = np.array([ [11, 12, 13], [21, 22, 23] ])
print("shape of matrixA = ", np.shape(matrixA))

#%%

print( matrixA[2, 3]) # error index out of bound will occur because we are accessing out of the boundaries of the declared numpy array

#%%

print(matrixA[0,1])

#%%

print(matrixA[5,5]) # again index out of bound error

#%%

matrixA[1, 2] = 99.
print(f"{matrixA}")

#%%

matrixA[1, 2] = 99. 
print(f"{matrixA=}")

#%%

Nx = 50
Ny = 30

#1-D coordinate arrays

x = np.linspace(0., 4., Nx)
y = np.linspace(-1.,1.,Ny)

#2-D coordinate arrays to address All vertex coordinates

x2d = np.zeros((Nx, Ny))
y2d = np.zeros((Nx, Ny))

#fill in the coordinate values in 2-D arrays 

for j in range(Ny):
    for i in range(Nx):
        x2d[i,j] = x[i]
        y2d[i,j] = y[j]

#plot as scatter

pl.plot(x2d, y2d, 'bo',mfc = 'none')

#using meshgrid function of numpy library

x2dMG, y2dMG = np.meshgrid(x, y)

#plot as scatter

pl.plot(x2dMG, y2dMG ,'r+')

#%%

#store grid to file (human readable)

path = '/home/lubuntu/Downloads'
np.savetxt(path + 'uniform_x2d.csv', x2d, delimiter=',')
np.savetxt(path + 'uniform_y2d.csv', y2d, delimiter=',')
