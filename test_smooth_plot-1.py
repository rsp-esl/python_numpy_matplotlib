#!/usr/bin/env python

import time, sys
import numpy as np 
import matplotlib.pyplot as plot
from scipy.signal import lfilter  # IIR filter

N = 100

ts = np.linspace( -2*np.pi, 2*np.pi, num=N )
data = (1+np.random.rand(N)/10.0) * np.sin( np.linspace(-2*np.pi,2*np.pi,N) ) 

def iit_filter(x):
   n = 9 
   b = [1.0 / n] * n
   a = 1
   m = int(n/2)
   x = np.append(x, np.zeros(2*m) + x[-1]) 
   y = lfilter(b,a,x)
   return y[m:-m]

def smooth_filter(x):
   window = 'hanning'
   window_len = 11
   s=np.r_[x[window_len-1:0:-1],x,x[-2:-window_len-1:-1]]
   w=eval('np.'+window+'(window_len)')
   y=np.convolve(w/w.sum(),s,mode='valid')
   half_len = int(window_len/2)
   return y[half_len:N+half_len]

#data2 = iit_filter(data)
data2 = smooth_filter(data)
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
