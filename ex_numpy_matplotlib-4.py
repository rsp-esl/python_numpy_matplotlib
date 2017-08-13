#!/usr/bin/env python
# Date: 2017-08-14
# Author: rsp @ Embedded Systems Lab (ESL), KMUTNB, Bangkok/Thailand

import numpy as np
import matplotlib.pyplot as plt

t_min = -2; t_max = 2; t_steps = 500
t = np.linspace( t_min, t_max, t_steps+1 )

# Method 1: using the NumPy Piecewise function
# see: https://docs.scipy.org/doc/numpy/reference/generated/numpy.piecewise.html
unit_step = lambda t: np.piecewise(t, [t < 0, t==0, t >= 0], [0, 0.5, 1])
x = unit_step(t)

# Method 2: using the NumPy Heaviside function
# see: https://docs.scipy.org/doc/numpy/reference/generated/numpy.heaviside.html
#x = [np.heaviside(_t,0.5) for _t in t]

lines = plt.plot( t, x )
plt.setp( lines, 'linewidth', 2.0, 'label', r'u(t)' )
plt.xlabel('Time t')
plt.ylabel('x(t) = u(t)')
plt.axis([t_min, t_max, -0.5, 1.5])
plt.grid(True)
plt.legend( bbox_to_anchor=(0.95, 1.0), loc='upper right' )
plt.savefig('figure-4.png')
plt.show()

#############################################################
