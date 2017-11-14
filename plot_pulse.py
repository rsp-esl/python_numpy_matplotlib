#!/usr/bin/env python

###############################################################################
## Author: Rawat S. (KMUTNB, Bangkok/Thailand)
## Date: 2017-10-27
###############################################################################

import numpy as np
from sympy import *
import matplotlib.pyplot as plt
t = symbols('t', real=True)
u = lambda t: Piecewise( (1, t >= 0), (0, True) )
pulse = lambda t: u(t+1) - u(t-1)
plt.style.use(['bmh'])
plt.rc('figure', figsize=(10, 6), autolayout=True)
plt.rc('grid', c='0.5', ls='-', lw=0.5)
plt.rc('axes', axisbelow=True, grid=True)
p = plot( pulse(t),(t,-2,2), show=False, legend=False );
p.title = 'Plot Rectangular Pulse: $u(t+1) - u(t-1)$';
p.xlabel = None; p.ylabel = None;
p.ylim = (-0.2, 1.2); p.xlim = (-2.0, 2.0);
p.save( "plot_pulse.png" )
p.show()

###############################################################################
