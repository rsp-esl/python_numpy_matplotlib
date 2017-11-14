#!/usr/bin/env python

###############################################################################
## Author: Rawat S. (KMUTNB, Bangkok/Thailand)
## Date: 2017-10-23
###############################################################################

import matplotlib.pyplot as plt
import numpy as np

tm = 1.500; t_step = 0.001
t = np.arange( -tm+2*t_step, tm+2*t_step, t_step )
T = 1.0  # period (in sec)
square_wave = lambda t: np.piecewise(t, [(t%T) < T/2,(t%T) > T/2],[1,-1])
plt.plot( t, square_wave(t) )
plt.xlabel( 't [sec]' )
plt.ylabel( 'x(t)' )
plt.title( 'Plot square wave (Period T=%.1f)' % T )
plt.grid( True )
ax = plt.gca()
major_ticks = np.arange(-tm, tm, 0.5)
minor_ticks = np.arange(-tm, tm, 0.1)   
ax.set_yticks( major_ticks ) 
ax.set_yticks( minor_ticks, minor=True ) 
plt.savefig( 'plot_square_wave_T%.1f.png' % T )
plt.show()

###############################################################################
