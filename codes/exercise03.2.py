#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 12 21:32:32 2025

@author: lubuntu
"""
import numpy as np
import matplotlib.pyplot as pl
Nx=50
Ny=30
#1_D coordinate arrays
x=np.linspace(0.,4.,Nx)
#y=np.linspace(0.,1.,Ny)
#y=np.linspace(0.,1.,Ny) #replace by stretched coordinate
#normalized "grid coordinate"
xi=np.linspace(0.,1.,Ny)
#define stretching function
def symmetric_stretching(xi,a=0.99):
    b=0.5*np.log((1.+a)/(1.-a))
    y=np.tanh(b*(xi-0.5))/np.tanh(0.5*b)
    return y
def unstretched(xi):
    y=2.*xi-1. 
    return y 
#apply stretching
y=symmetric_stretching(xi,a=0.99)
y_unstretched=unstretched(xi)   
#plot stretching function
pl.figure(1)
pl.plot(xi,y_unstretched,'b--',lw=2,label='unstretched')
pl.plot(xi,y,label='symm.stretch')
pl.legend()
pl.grid()
#%%
#generate 2d mesh(see previous exercise)
x2d,y2d=np.meshgrid(x,y)
#plot 2d mesh
pl.figure(2)
pl.plot(x2d,y2d,'r+')
pl.show()
#%%
#load the uniform 2d mesh from previous tsak
path="/home/lubuntu/"
x2d_uniform=np.loadtxt(path+'uniform_x2d.csv',delimiter=',')
y2d_uniform=np.loadtxt(path+'uniform_y2d.csv',delimiter=',')
#plot 2d mesh
pl.figure(2)
pl.plot(x2d_uniform,y2d_uniform,'bs',mfc='None')
#pl.grid()
pl.show()

