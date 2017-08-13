#!/usr/bin/env python
# Date: 2017-08-14
# Author: rsp @ Embedded Systems Lab (ESL), KMUTNB, Bangkok/Thailand

import numpy as np
import matplotlib.pyplot as plt

t_min = -4; t_max = 4; t_steps = 500
t = np.linspace( t_min, t_max, t_steps+1 )

# see: https://docs.scipy.org/doc/numpy/reference/generated/numpy.piecewise.html
x = lambda t,T: np.piecewise(t, [(t >= 0) & (t < T)], [lambda t: t, 0])
T = 2
x1 = x(t,T)
x2 = x(-t,T)
x3 = x(t+1,T)
x4 = x(-1-t,T)

fig, axes = plt.subplots(nrows=2, ncols=2,figsize=(8,5),dpi=100)

ax = axes[0][0]
#ax = plt.subplot(221)
ax.plot( t, x1 )
ax.set_xlabel( 'Time t' )
ax.set_ylabel( r'$x_1(t) = x(t)$' )
ax.grid(True)
ax.set_ylim(-1,3)
ax.set_xlim(t_min,t_max)

#ax = axes[0][1]
ax = plt.subplot(222)
ax.plot( t, x2 )
ax.set_xlabel( 'Time t' )
ax.set_ylabel( r'$x_2(t) = x(-t)$' )
ax.grid(True)
ax.set_ylim(-1,3)
ax.set_xlim(t_min,t_max)

#ax = axes[1][0]
ax = plt.subplot(223)
ax.plot( t, x3 )
ax.set_xlabel( 'Time t' )
ax.set_ylabel( r'$x_3(t) = x(t+1)$' )
ax.grid(True)
ax.set_ylim(-1,3)
ax.set_xlim(t_min,t_max)

#ax = axes[1][1]
ax = plt.subplot(224)
ax.plot( t, x4 )
ax.set_xlabel( 'Time t' )
ax.set_ylabel( r'$x_4(t) = x(-1-t)$' )
ax.grid(True)
ax.set_ylim(-1,3)
ax.set_xlim(t_min,t_max)

plt.tight_layout(pad=1.0, w_pad=1.0, h_pad=1.0)
fig.savefig('figure-6.png')
plt.show()

#############################################################
