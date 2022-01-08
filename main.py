"""
Ntigkaris E. Alexandros
Python v.3.9.2

Comparing numerical differentation methods' efficiencies.
"""

import numpy as np
import pandas as pd

h0 = 0.01

def dydx_central(y,xo,h=h0):
    return (y(xo+h) - y(xo-h))/(2*h)
    # return (-y(xo+2*h)+8*y(xo+h)-8*y(xo-h)+y(xo-2*h))/(12*h)

def dydx_forward(y,xo,h=h0):
    # return (y(xo+h) - y(xo))/h
    return ( -y(xo+2*h)+4*y(xo+h)-3*y(xo))/(2*h)

def dydx_backward(y,xo,h=h0):
    # return (y(xo) - y(xo-h))/h
    return (3*y(xo)-4*y(xo-h)+y(xo-2*h))/(2*h)

F = np.array([10.889365,12.703199,14.778112,17.148957,19.855030])
x = np.array([1.8,1.9,2.0,2.1,2.2])

y = lambda x: x*np.exp(x)
dydx = lambda x: (x+1)*np.exp(x)

cntr = [dydx_central(y,i) for i in x]
fwrd = [dydx_forward(y,i) for i in x]
bwrd = [dydx_backward(y,i) for i in x]
dydx = [dydx(i) for i in x]
errc = [((abs(dydx[i] - cntr[i])/cntr[i]))*100 for i in range(len(x))]
errf = [((abs(dydx[i] - fwrd[i])/fwrd[i]))*100 for i in range(len(x))]
errb = [((abs(dydx[i] - bwrd[i])/bwrd[i]))*100 for i in range(len(x))]

table = pd.DataFrame({"x":x,"f(x)":F,"f'(x)":dydx,"Central":cntr,"Forward":fwrd,"Backward":bwrd,"Error(cntrl)":errc,"Error(fwrd)":errf,"Error(bwrd)":errb})
print(table)