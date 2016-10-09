import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D	
from sympy import *

def qfun(z):
	res = (- z*z  / 8.0 / np.pi + 1.0 / 256.0 / np.pi / np.pi / np.pi + 1.0 / 32.0 / np.pi) * np.cos(8.0 * np.pi * z) + 1.0 / 32.0/np.pi / np.pi * z * np.sin(8.0 * np.pi * z)
	return res	

def qder1st(z):
	#res = 1.0 / 32.0 / np.pi / np.pi * np.sin(8 * np.pi * z) - 8.0 * np.pi * np.sin(8*np.pi * z) * (- z*z  / 8.0 / np.pi + 1.0 / 256.0 / np.pi / np.pi / np.pi + 1.0 / 32.0 / np.pi)
	res = z*z*np.sin(8.0*np.pi*z) - np.sin(8.0*np.pi*z)/4.0
	return res

def qder2nd(z):
	res = 2.0*z*np.sin(8.0*np.pi*z) - 2.0*np.pi*np.cos(8.0*np.pi*z) + 8.0*z*z*np.pi*np.cos(8.0*np.pi*z)
	return res

def func(x1, x2):
	res = 1.0 + 4.0 * (qder2nd(x1) * qfun(x2) + qder2nd(x2) * qfun(x1)) + 16.0 * (qfun(x1)*qfun(x2)*qder2nd(x1)*qder2nd(x2) - qder1st(x1)*qder1st(x1)*qder1st(x2)*qder1st(x2))	
	return res




eps = 1e-10	
a=qfun(1.0/16.0)
b=qfun(1.0/16.0+eps)
c=qfun(1.0/16.0-eps)
der = (b-a) / eps
dera = qder1st(1.0/16.0)

dera2 = qder2nd(1.0/16.0)

print "result", der, dera
print "result", (b-2.0 * a + c) / eps/eps , dera2


x1 = np.arange(-0.5, 0.5, 0.001)
x2 = np.arange(-0.5, 0.5, 0.001)

fig = plt.figure()
ax = fig.gca(projection='3d')
X, Y = np.meshgrid(x1, x2)
f=func(x1,x2)
surf = ax.plot_surface(X, Y, f, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

plt.show()

