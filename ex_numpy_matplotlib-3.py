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

fig, axes = plt.subplots(nrows=2,figsize=(5,4), dpi=150)
axes[0].plot( t, x1, label=r'$sin(\frac{2\pi}{5} t)$' )
axes[1].plot( t, x2, label=r'$cos(\frac{2\pi}{5} t)$'  )
axes[0].grid(True)
axes[1].grid(True)
fig.savefig('figure-3.png')
plt.show()

#############################################################
