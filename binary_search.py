#Bisection Search
#MATH F313: Numerical Analysis
from math import e

def f(x):
    return 5*e**-x + x - 5

import pylab as plt
import numpy as np

def inspect():
    #Function to inspect the possible positions of roots
    a = np.linspace(-2,1.5,100)
    b = f(a)
    plt.plot(a,b)
    plt.show()
    
x1, x2 = -2, 1.5 # bracket values (x1,x2) = (-2,1.5)
error = 1e-6 # permissible error

i = 0 # iteration counter

while abs(x1-x2)>error and i < 200:
    x3 = .5 * (x1+x2)
    if f(x1)*f(x3) < 0:
        x2 = x3
    elif f(x2)*f(x3) < 0:
        x1 = x3
    i+=1 
    
rt = 0.5 * (x1 + x2) # estimated root of the equation
      
print 'The root of the equation is ' + str(rt) + '\n' + 'f(root) = ' + str(f(rt))
print 'No. of iterations: ' + str(i)