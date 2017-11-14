#!/usr/bin/env python

###############################################################################
## Author: Rawat S. (KMUTNB, Bangkok/Thailand)
## Date: 2017-10-23
###############################################################################

import matplotlib.pyplot as plt
import numpy as np

tm = 1.500; t_step = 0.001
t = np.arange( -tm+2*t_step, tm+2*t_step, t_step )
N = 50; y = 0
for k in range(N):
     y = y + np.sin( 2*np.pi*(2*k+1)*t )/(2*k+1) 
plt.plot( t, (4 * y) / np.pi )
plt.xlabel( 't [sec]' )
plt.ylabel( 'x(t)' )
plt.title( 'Plot Square Wave: Fourier Series (N=%d)' % N )
plt.grid( True )
ax = plt.gca()
major_ticks = np.arange( -tm, tm, 0.5 )
minor_ticks = np.arange( -tm, tm, 0.1 )   
ax.set_yticks( major_ticks ) 
ax.set_yticks( minor_ticks, minor=True ) 
plt.savefig( "plot_fs_square_wave_N%d.png" % N )
plt.show()

###############################################################################
