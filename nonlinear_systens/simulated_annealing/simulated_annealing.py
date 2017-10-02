import numpy as np 
from math import *
from random import random,randint


def energy(x):
	return abs(x[0]**2 - 2*x[0] + x[1]**2 - x[2] + 1) 
	#x[0]*x[1]**2 - x[0] - 3*x[1] + x[1]*x[2] + 2 
	#x[0]*x[2]**2 -3*x[2] + x[1]*x[2]**2 + x[0]*x[1]
	#return abs(2*x[0]**2 + x[1]**2)

def getGaussDisturbio(mu,sigma,dim):
	gd = np.array(dim*[0.0])
	#[gd.__setitem__(i,sqrt(-2*log(random()))*cos(2*pi*random())*sigma + mu) for i in range(dim)]
	#[gd.__setitem__(i,sqrt(-2*log(random()))*cos(2*pi*random())*sigma + mu) for i in range(randint(0,dim))]
	[gd.__setitem__(i,sqrt(-2*log(random()))*cos(2*pi*random())*sigma*random() + mu) for i in range(randint(0,dim))]
	return gd

x = np.array([10.0,10.0,10.0])
T = 1000
mu = 0
sigma = 1
alpha = 0.9
error = 1e-4
while energy(x) > error:
	xi = np.array(x + getGaussDisturbio(mu,sigma,len(x)))
	delta = energy(xi) - energy(x)
	if(delta < 0):
		x = xi
	else:
		if(exp(-delta/T) > random()):
			x = xi
	print(x,xi,energy(x))
	T = alpha*T