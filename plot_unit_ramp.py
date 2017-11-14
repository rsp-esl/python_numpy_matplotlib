#!/usr/bin/env python

###############################################################################
## Author: Rawat S. (KMUTNB, Bangkok/Thailand)
## Date: 2017-10-27
###############################################################################

import numpy as np
from sympy import *
import matplotlib.pyplot as plt
t = symbols('t', real=True)
plt.style.use(['bmh'])
u = lambda t: Piecewise( (1, t >= 0), (0, True) )
r = lambda t: t*u(t)
plt.rc('figure', figsize=(10, 6), autolayout=True)
plt.rc('axes', labelsize=10, titlesize=10)
p = plot( r(t),(t,-2,2), show=False, legend=False, axis=True );
p.title = 'Plot Ramp Function: $r(t) = t u(t)$';
p.xlabel = None; p.ylabel = None;
p.ylim = (-0.5, 2.0); p.xlim = (-2.0, 2.0);
p.save( "plot_unit_ramp.png" )
p.show()

###############################################################################
