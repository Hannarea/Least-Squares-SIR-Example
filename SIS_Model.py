# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 18:55:05 2021

@author: hreed
"""

import numpy as np
from Utils.Simulate import simulate


# This model has two strains of a disease
def model(y, x, beta1, beta2, gamma1, gamma2, mu):
    dSdt = -(beta1*y[1]+beta2*y[2])*y[0] + (gamma1 + mu)*y[1] +(gamma2 + mu)*y[2]
    dI1dt = beta1*y[1]*y[0] - (gamma1 + mu)*y[1]
    dI2dt = beta2*y[2]*y[0] - (gamma2 + mu)*y[2]
    
    return dSdt, dI1dt, dI2dt


y0 = np.array([100, 1, 1])
beta1, beta2, gamma1, gamma2, mu = 0.003, 0.003, 0.0999, 0.1, 0.01
t = np.linspace(0,100000,100001)
labels = ['Susceptibles', 'Strain 1', 'Strain 2']

y = simulate(model, y0, t, (beta1, beta2, gamma1, gamma2, mu), labels)