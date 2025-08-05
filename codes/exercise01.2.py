# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 21:45:59 2025

@author: faral
"""

#from numpy import sin
import numpy as np
import matplotlib.pyplot as pl

# generate the 1D grid
x = np.linspace(0., 1., 11)
h = x[1] - x[0]	# stepsize

#function implementations, also keep in mind that numpy is a very good library for numeircal computations 
y1 = 1. - 2*x # this is function f_1(x)
y2 = (x - 0.4)**2 # this is function f_2(x)
y3 = np.sin(2 * np.pi * x) # this is function f_3(x)

# filtering of data
xFiltered = x[ x <= 0.5 ] # filtered means we want to extract specific portion from the data, also we can also put logical expression inside the array to pick specific values, the example of it will look like x[x<0.5] so all the values which are less than 0.5 will be picked 

y3Filtered = y3[ x <= 0.5 ]

# plot data according tasks
pl.figure(1)

pl.plot(x, y1, 'r--', label='f_1') # alternative for label is label='$f_1(x)$'
pl.plot(x, y2, 'b-',  label='f_2') # label='$f_2(x)$'
pl.plot(x, y3, 'g:',  label='f_3') # label='$f_3=\sin(2 \pi x)$'

#by above 3 commands, we will get 3 plotting commands
pl.grid()
pl.xlabel('x')
pl.ylabel('y')
pl.title('Figure 1')

pl.legend()
# pl.xlim([0.2 ,0.6])

pl.figure(2)
pl.plot(xFiltered, y3Filtered, 'go',label= 'f_3 filtered')
pl.xlabel('x') 
pl.ylabel('y')
pl.title('Figure 2')

#we can also write this instead of the above line of code
#pl.plot(x[x<=0.5],y3[x<=0.5],'go',label='f_3 filtered') 
#this is like filtering data on the base of mask

pl.figure(3)
pl.plot(x, y1, 'r--', label='f_1') # alternative for label is label='$f_1(x)$'
pl.plot(x, y2, 'b-',  label='f_2') # label='$f_2(x)$'
pl.plot(x, y3, 'g:',  label='f_3') # label='$f_3=\sin(2 \pi x)$'

pl.plot(xFiltered, y3Filtered, 'go', label='f_3 filtered')

pl.xlabel('x')
pl.ylabel('y')
pl.title('Figure 3')

pl.grid()
pl.legend()

pl.show()