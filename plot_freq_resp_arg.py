#!/usr/bin/env python

###############################################################################
## Author: Rawat S. (KMUTNB, Bangkok/Thailand)
## Date: 2017-10-27
###############################################################################

import numpy as np
from sympy import *
import matplotlib.pyplot as plt
f = symbols('f', real=True)
H = lambda f: 1/(1+I*(2*pi*f/1000))  # omega_0 = 10^3
plt.rc('figure', figsize = (10, 6))  
plt.rc('figure', autolayout = True)
plt.rc('axes', labelsize=10, titlesize=12)
p = plot( arg(H(f)),(f,-2000,2000), show=False, legend=False, axis=True );
p.title = 'Plot'; p.xlabel = 'f [Hz]'; p.ylabel = 'arg[H(f)]';
p.ylim = (-np.pi/2,np.pi/2); p.xlim = (-2000,2000);
p.xscale = 'linear';
p[0].line_color = 'blue';
p.save( "plot_freq_resp_arg.png" )
p.show()

###############################################################################
