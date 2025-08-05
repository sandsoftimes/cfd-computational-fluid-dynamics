#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 03:53:13 2025

@author: lubuntu
"""

# modules
import matplotlib.pyplot as pl
import numpy as np

# parameters 
s = 10.
r = 28.
b = 8./3. 

tEnd = 40  # sec
dt = 1.e-3 # sec

# initial condition
t0 =  0.    #sec
x0 = -8. 
y0 = -1. 
z0 = 33. 

# make room for data storage, fill in initial condition
tValues = [t0]
xValues = [x0]
yValues = [y0]
zValues = [z0]

# initializing parameters for loop
t = t0
x = x0 
y = y0
z = z0

# time loop
while t <= tEnd:
    # explicit Euler (lower sum), just one step from n to n+1 for variables
    
    #xNew = x + Rx * dt
    #yNew = y + Ry * dt
    #zNew = z + Rz * dt
    
    xNew = x + ( s*(y-x)     )     * dt
    yNew = y + ( (r-z)*x - y )     * dt
    zNew = z + ( x*y - b*z   )     * dt
    
    # time update
    tNew = t + dt
    
    # synchronize
    x = xNew
    y = yNew 
    z = zNew
    t = tNew
    
    # append new values to the data storage list
    tValues.append(t)
    xValues.append(x)
    yValues.append(y)
    zValues.append(z)

# convert simulation results to numerical array
tValues = np.array(tValues)
xValues = np.array(xValues)
yValues = np.array(yValues)
zValues = np.array(zValues)

#%%
path = '/home/lubuntu/' # give the path here where you want to save
np.save(path+'tValues', tValues)
np.save(path+'xValues', xValues)
np.save(path+'yValues', yValues)
np.save(path+'zValues', zValues)

checksum = xValues.sum()
print(f'{checksum=}')

# plot the data
pl.figure(1)
pl.plot(tValues, xValues, 'b-') # time series x(t) at discrete times
pl.plot(tValues, yValues, 'r-') # time series y(t) at discrete times
pl.plot(tValues, zValues, 'g-') # time series z(t) at discrete times

pl.xlabel('$t$')
pl.ylabel('$x, y, z$')

pl.figure(2)
pl.plot(xValues, yValues, 'k-') # parametric plot x(t) vs. y(yt) co-relation between two dynamic variables

pl.xlabel('$x$')
pl.ylabel('$y$')

#%%

# multiple subplots

pl.figure(3)
fig, axs = pl.subplots(2, 2)
axs[0, 0].plot(xValues, yValues, 'k-')
axs[0, 0].set_xlabel('x')
axs[0, 0].set_ylabel('y')

axs[0, 1].plot(xValues, zValues, 'b-')
axs[0, 1].set_xlabel('x')
axs[0, 1].set_ylabel('z')

axs[1, 0].plot(yValues, zValues, 'r-')
axs[1, 0].set_xlabel('y')
axs[1, 0].set_ylabel('z')

axs[1,1].plot(xValues+yValues, xValues-yValues, 'g-')
axs[1,1].set_xlabel('x+y')
axs[1,1].set_ylabel('x-y')

#%%

# 3-D plot

fig = pl.figure(4)
ax = fig.add_subplot(111, projection='3d')

ax.plot(xValues+yValues, xValues-yValues, zValues, 'r-')

ax.set_xlabel('x+y')
ax.set_ylabel('x-y')
ax.set_zlabel('z')

pl.show()