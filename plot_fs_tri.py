#!/usr/bin/env python

###############################################################################
## Author: Rawat S. (KMUTNB, Bangkok/Thailand)
## Date: 2017-10-23
###############################################################################

import matplotlib.pyplot as plt
import numpy as np

tm = 1.500; t_step = 0.001
t = np.arange( -tm+2*t_step, tm+2*t_step, t_step )
N = 10; y = 0
for k in range(N):
     y = y + np.cos( 2*np.pi*(2*k+1)*t )/((2*k+1)*(2*k+1)) 
plt.plot( t, 0.5 + 4*y/(np.pi*np.pi) )
plt.xlabel( 't [sec]' )
plt.ylabel( 'x(t)' )
plt.title( 'Plot Triangular Wave (N=%d)' % N)
plt.grid( True )
ax = plt.gca()
major_ticks = np.arange( -0.2, 1.3, 0.2 )
minor_ticks = np.arange( -0.2, 1.2, 0.1 )   
ax.set_yticks( major_ticks ) 
ax.set_yticks( minor_ticks, minor=True ) 
plt.savefig( "plot_tri_N%d.png" % N )
plt.show()

###############################################################################
