#!/usr/bin/env python

import time, sys
import numpy as np 
import matplotlib.pyplot as plot
import scipy as sp
from scipy import signal

N = 100

ts = np.linspace( -2*np.pi, 2*np.pi, num=N )
data = (1+np.random.rand(N)/10.0) * np.sin( np.linspace(-2*np.pi,2*np.pi,N) ) 

def median_filter(x):
     y = sp.signal.medfilt(x,7)
     return y

data2 = median_filter(data)
plot.figure(figsize=(12, 4), dpi=100)
plot.plot(ts, data, ts, data2 )
plot.title( 'Plot f(t)')
plot.ylabel( 'f(t)' )
plot.xlabel( 't' )
plot.grid(True)
plot.savefig( 'plot.png',dpi=200,bbox_inches='tight' )
plot.show()

time.sleep(1.0)
print('Done....')

############################################################################
