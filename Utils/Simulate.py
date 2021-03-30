# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 14:19:41 2021

@author: hreed
"""

from scipy import integrate
import matplotlib.pyplot as plt
import numpy as np

# simulate simulates the give model, intended for use as a module


def simulate(model, y0, t, parameters, labels):
    """
    model : the model we are simulating 
    y0 : the initial population sizes
    t : the time we are running the simulations over 
    parameters : parameters that are needed for the model
    
    returns the simulations from integrate.odeint
    """
    y = integrate.odeint(model, y0, t, args = parameters)
    for i in range(len(y[0,:])):
        plt.plot(y[:,i], label = labels[i])
    plt.title("Simulations")
    plt.ylabel("Population")
    plt.xlabel("Time")
    plt.legend()
    plt.show()
    return y
       

# An example on how to use:
def model(y, t, beta, gamma):
    dSdt = -beta*y[0]*y[1]
    dIdt = beta*y[0]*y[1] - gamma*y[1]
    dRdt = gamma*y[1]
    return dSdt, dIdt, dRdt

y0 = np.array([10, 1, 0])
t = np.linspace(0,10,100)
beta, gamma = 0.33, 0.1
labels = ['sus', 'inf', 'rec']

y = simulate(model, y0, t, (beta, gamma), labels)


    






 