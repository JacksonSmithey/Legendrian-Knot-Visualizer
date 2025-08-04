# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 00:32:03 2024

@author: Jackson
"""

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def main():
    print("Please hold...")
    x = sp.Symbol('x')
    e1 = sp.Symbol('e1')
    print(x, e1)
    #X,E1 = np.meshgrid(x,e1)
    #print(X, E1)
    
    f = sp.Function('f')(x, e1)
    f = (4-x**2)*e1 - e1**3
    dfe = sp.diff(f,e1)
    dfx = sp.diff(f,x)
    
    #zerograd = sp.grad(f)
    #xdata = sp.N(zerograd.x)
    
    #for i in range(xdata-3, xdata+3, .1):
        #newpoints = sp.solve(x==i, dfe(x,e1) == 0)
        
        

    #fig = plt.figure(figsize=(xdata-3,xdata+3))
    #ax = fig.add_subplot(111, projection='3d')
    
    # syntax for 3-D projection
    ax = plt.axes(projection ='3d')
 
    # defining all 3 axis
    x = x
    z = sp.nonlinsolve(f)
    y = dfx
     
    # plotting
    ax.scatter(x, y, z)
    ax.set_title('Generating family: ' + str(f))
    plt.show()
    
    # Plot a 3D surface
    #ax.plot_surface(x, Y, f)

    print("Program complete!")

if __name__ == '__main__':
    main()
