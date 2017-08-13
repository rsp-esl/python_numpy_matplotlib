#!/usr/bin/env python
# Date: 2017-08-14
# Author: rsp @ Embedded Systems Lab (ESL), KMUTNB, Bangkok/Thailand

import numpy as np
import matplotlib.pyplot as plt

pi  = np.pi
sin = np.sin

t_min = -2*pi; t_max = 2*pi; t_steps = 200
t = np.linspace( t_min, t_max, t_steps+1 )
x = sin(2*pi*t/5)

plt.plot( t, x, linewidth=2.0 )
plt.title( r'$x(t) = sin(\frac{2 \pi}{5} t)$' )
plt.xlabel('Time t')
plt.ylabel('x(t)')
plt.axis([t_min, t_max, -1.25, 1.25])
plt.grid(True)
plt.savefig('figure-1.png')
plt.show()

#############################################################

