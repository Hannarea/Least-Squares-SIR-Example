# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 19:59:51 2021

@author: hreed
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate, optimize

# Here is the data we are going to fit:
# infectives I at time t
time = np.linspace(0,10,10)
infectives = np.array([1. , 8.6556056 , 9.37871953 , 8.44328311 ,
                       7.55728868 , 6.76265894 , 6.05150019 , 
                       5.41512095 , 4.84566321 , 4.33608991])
# Known inital conditions:
y0 = np.array([10, 1, 0])

# the true best parameters are beta = 0.33 and gamma = 0.1

# Define the model
# computes the values in y at time t
def model(y, t, beta, gamma):
    dSdt = -beta*y[0]*y[1]
    dIdt = beta*y[0]*y[1] - gamma*y[1]
    dRdt = gamma*y[1]
    return dSdt, dIdt, dRdt

# Sum of Squares
# x : vector of parameters to be fit 
# d : vector of data to be fit
# t : time for the data
def SS(x, t, y0, data):
    #find the current solution
    y = integrate.odeint(model, y0, t, args = (x[0], x[1])) 
    #calculate and return the sum of the squares of the residuals
    return sum((data - y[:,1])**2)

# minimizes the sum of squares function
# x0 : initial guess for the parameter values 
# currently no bounds on parameters
def LS(x0, t, y0, data):
    m = optimize.minimize(SS, x0, args = (t, y0, data))
    return m


# initial guess
x0 = np.array([0,0])
t = np.linspace(0,10,10)
m = LS(x0, t, y0, infectives)

print('these are the best fit parameters [beta, gamma]: ',m.x)


# get the solutions using the parameters found with LS
t = np.linspace(0, 10, 100)
y = integrate.odeint(model, y0, t, args = (m.x[0], m.x[1]))

# plot the data
plt.plot(np.linspace(0,len(infectives), len(infectives)), infectives, 'ro', label = 'Data')

# plot the solutions
plt.plot(t, y[:,0], 'b', label = 'Susceptibles')
plt.plot(t, y[:,1], 'r', label = 'Infectives')
plt.plot(t, y[:,2], 'g', label = 'Recovered')
plt.ylabel('Individuals')
plt.xlabel('Days')
plt.title('Simulations')
plt.legend()
plt.show()

