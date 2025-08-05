#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 17:24:23 2025

@author: lubuntu
"""
5 + 5

5

'hello' + ' ' + 'world'

print(5+5)

print('result: ', 5+5, '!')

print("result: 5+5 !")

print('result: %0i'   % (5+5)) 

print('result: %0i'   % (5+4))

print('result: %05i'  % (5+4))

print('result: %1.2f' % (5+4))

print(f'result: {5+4}')

print('hello world!')

#%%

x = 5 
print(f'x = {x}')

y = 9.345 

myString = 'hello world '

#%% 

print(f'before {x}')
x = x+2.5
print(f'after {x}')

#%%

from numpy import sin 
import numpy as np 
import matplotlib.pyplot as pl 

print(np.sin(1.))

x  = np.linspace(0., 1., 11)

y1 = 1. -2*x 
y2 = (x - 0.4) ** 2
y3 = np.sin(2. * np.pi * x)

pl.plot(x, y1, 'r--', label='f_1') # red dashed line
pl.plot(x, y2, 'b:',  label='f_2') # blue dashed line
pl.plot(x, y3, 'g-',  label='f_3') # green dashed line

pl.xlabel('x')
pl.ylabel('y')
pl.title('Figure 1')

pl.grid()

pl.legend()

#pl.xlim([0.2, 0.8])

pl.ylim([-1.2, 1.2])

pl.show()



