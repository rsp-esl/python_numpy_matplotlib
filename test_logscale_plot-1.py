#!/usr/bin/env python

import time, sys
import numpy as np 
import matplotlib.pyplot as plot
import scipy as sp
from scipy import signal

N = 100

ts = [ pow(2,i-10) for i in range(0,20)]
data = np.exp(-(np.array(ts))/5.0)

plot.figure(figsize=(12, 4), dpi=100)
#plot.semilogx(ts, data )
plot.plot( ts, data)
plot.xscale('log')
plot.title( 'Plot f(t)')
plot.ylabel( 'f(t)' )
plot.xlabel( 't' )
plot.grid(True)
plot.savefig( 'plot.png',dpi=200,bbox_inches='tight' )
plot.show()

time.sleep(1.0)
print('Done....')

############################################################################
