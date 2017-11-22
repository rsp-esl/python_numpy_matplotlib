#!/usr/bin/env python

import time, sys
import numpy as np 
import matplotlib.pyplot as plot
import scipy as sp
from scipy import signal

N = 100

ts = np.logspace(start=-1,stop=5,num=200, base=10)
data = 1/(np.square(0.01*ts - 100.0/ts) + 0.1)

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
