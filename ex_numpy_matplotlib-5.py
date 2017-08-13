#!/usr/bin/env python
# Date: 2017-08-14
# Author: rsp @ Embedded Systems Lab (ESL), KMUTNB, Bangkok/Thailand

import numpy as np
import matplotlib.pyplot as plt

t_min = -2; t_max = 2; t_steps = 500
t = np.linspace( t_min, t_max, t_steps+1 )

# see: https://docs.scipy.org/doc/numpy/reference/generated/numpy.piecewise.html
ramp = lambda t: np.piecewise(t, [t < 0, t >= 0], [0, lambda t: t])
x = ramp(t)

lines = plt.plot( t, x )
plt.setp( lines, 'linewidth', 2.0, 'label', r'x(t) = t u(t)' )
plt.xlabel('Time t')
plt.ylabel('x(t)')
plt.axis([t_min, t_max, -0.5, 2.0])
plt.grid(True)
plt.legend( bbox_to_anchor=(0.9, 1.0), loc='upper right' )
plt.savefig('figure-5.png')
plt.show()

#############################################################

