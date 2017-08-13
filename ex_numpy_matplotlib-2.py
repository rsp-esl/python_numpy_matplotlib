#!/usr/bin/env python
# Date: 2017-08-14
# Author: rsp @ Embedded Systems Lab (ESL), KMUTNB, Bangkok/Thailand

import numpy as np
import matplotlib.pyplot as plt

pi  = np.pi
sin = np.sin
cos = np.cos

t_min = -2*pi; t_max = 2*pi; t_steps = 200
t = np.linspace( t_min, t_max, t_steps+1 )
x1 = sin(2*pi*t/5)
x2 = cos(2*pi*t/5)

lines = plt.plot( t, x1 )
plt.setp( lines, 'linewidth', 2.0, 'label', r'$sin(\frac{2\pi}{5} t)$' )
lines = plt.plot( t, x2 )
plt.setp( lines, 'linewidth', 2.0, 'label', r'$cos(\frac{2\pi}{5} t)$' )
plt.xlabel('Time t')
plt.ylabel('x(t)')
plt.axis([t_min, t_max, -1.25, 1.25])
plt.grid(True)
plt.legend( bbox_to_anchor=(0.95, 1.1), loc='upper right' )
plt.savefig('figure-2.png')
plt.savefig('figure-2.pdf', format='pdf', bbox_inches='tight')
plt.show()

#############################################################

