# -*- coding: utf-8 -*-
"""
Created on Wed Jul 30 06:16:31 2025

@author: faral
"""
import numpy as np
import matplotlib.pyplot as pl

def factorial(n):
	if n<=0:	
		return 1
	else:
		return n*factorial(n-1)
def taylor4(x):
	"""implements exp(-2*x-1) by 4th order taylor series"""
	return (1-2*(x+0.5)
		 +2*(x+0.5)**2
		 -8./6.*(x+0.5)**3
		 +16./24.*(x+0.5)**4)
def taylorN(x,N=4):
	y=np.zeros_like(x)
	for n in range(N+1):
		y+=(-2)**n/factorial(n)*(x+0.5)**n
	return y

def taylorNwithFunction(x,N=4):
	y=np.zeros_like(x)
	for n in range(N+1):
		y+=derivative(n)/factorial(n)*(x+0.5)**n
	return y

def derivative(n=1):
    if(n<=0):
        return 1
    else:
        return (-2)**n * np.exp(-2*-0.5-1)


#print(derivative(3))

#yN=taylorN(x,N=4) #uncomment it and run it and compare the result with our hard coded function taylor4(x), compare and see if both give same results


#%%

# Error calculation
N = 18
x = np.linspace(-1., 4., 21)
y4 = taylor4(x)
yN = taylorN(x, N)
# directly finding the value of exponential functional and comparing it with the value of our self defined function taylor() the results will be a bit different because we don't know upto which N (order of taylor series) should we take to make the results of both taylorN() and np.exp() equal
yR = np.exp(-2*x-1)

yWithfuntion = taylorNwithFunction(x, N=10)

abs_error = yN[-1] - yR[-1]
print('N = %i abs. error = %1.3e' % (N, abs_error))

#%%

# plotting
pl.plot(x,y4, label='$order_4$')
pl.plot(x,yN, label='$order_N$')
pl.plot(x,yR, label='$reference$')

pl.plot(x, yWithfuntion, 'b:', label='$new$')

#pl.xlim([-1,0])
#pl.ylim([0,2])	

pl.legend()
pl.grid()

pl.show()