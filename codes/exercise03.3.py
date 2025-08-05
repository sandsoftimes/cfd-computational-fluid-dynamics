#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 20 01:32:54 2025

@author: lubuntu
"""

import numpy as np
import matplotlib.pyplot as pl
from scipy.interpolate import griddata
#from numpy import random as rnd
#implement function f(x,y) in python
def data(x,y):
    return np.sin(2*np.pi*x)*np.cos(8*np.pi*y)*np.exp(-4*y**2)
#high resolution structured uniform cartesian grid
x1d=np.linspace(0.,1.,200)
y1d=np.linspace(0.,1.,200)
#2d meshgrid
x2d,y2d=np.meshgrid(x1d,y1d)
#get gridded data for 2d meshes
z2d=data(x2d,y2d)
#make a pseudo-color contour plot with 256 colour levels
pl.xlabel('$x$ axis')
pl.ylabel('$y$ axis')
pl.contourf(x2d,y2d,z2d,256)
pl.colorbar()
#now plot some random sampling points
points=np.random.random_sample((100,2))
print(points)
xpts=points[:,0]
ypts=points[:,1]
pl.plot(xpts,ypts,'ko')

#now get the low resolution data at sparse non-uniform sampling point

zpts = data(xpts, ypts)

#interpolate sampling point data to high-resolution grid for visualization

zpts_interp_2d = griddata((xpts, ypts), zpts, (x2d, y2d), method = 'linear') #methods = 'linear' or method = 'cublic' or method = 'nearest'

#plot interpolated values in a second figure

pl.figure(2)
pl.contourf(x2d, y2d, zpts_interp_2d, 256)

#plot random sampling points also in figure 2

pl.plot(xpts, ypts, 'ko')

#%%


zpts_interp_2d=griddata((xpts, ypts), zpts, (x2d, y2d), method = 'nearest')
pl.figure(3)
pl.contourf(x2d, y2d, zpts_interp_2d, 256)
pl.plot(xpts, ypts, 'ko')

#%%

zpts_interp_2d=griddata((xpts, ypts), zpts, (x2d, y2d), method = 'cubic')
pl.figure(4)
pl.contourf(x2d, y2d, zpts_interp_2d, 256)
pl.plot(xpts, ypts, 'ko')

