# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 18:59:36 2024

@author: Jackson
"""

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import plotly.graph_objects as go

def main():
    
    #User input
    #num_a = 0
    #num_e = 1
    
    #constants
    RES = 1
    ZOOM_ADDEND = 3
    VIEW_TEST_CODE = 1
    
    #Declare symbolic variables
    #a = sp.symbols('a:{}'.format(num_a))
    e = sp.Symbol('e', real=True)
    x = sp.Symbol('x', real=True)
    
    #Declare symbolic functions
    f = sp.Function('f')(x,e)
    #u = sp.Function('u:{}'.format(num_u))(x,e)
    #v = sp.Function('f')(x,e)
    
    #f = (4-x**2)*e - e**3
    f = (-1/3*e**3 + (4 - x**2)*(e+1))
    
    f = sp.simplify(f)
    print('f:', f)
    
    
    #Calculate dfe, dfx, gradient(f)
    dfe = sp.diff(f,e)
    dfx = sp.diff(f,x)
    if VIEW_TEST_CODE == 1:
        print('dfe:', dfe, type(dfe))
        print('dfx:', dfx, type(dfx))

     
    #Solve for gradient(f) = 0
    grad_f = [dfx, dfe]
    zerograd = sp.solve(grad_f, x, e)
    if VIEW_TEST_CODE == 1:
        print('zerograd:', type(zerograd), zerograd)
    
    xmin = 0
    xmax = 0
    
    #Find min and max of 0 gradient points
    for point in zerograd:        
        if isinstance(point[0], sp.Float) or isinstance(point[0], sp.Integer):
            if point[0] < xmin:
                xmin = point[0]
            if point[0] > xmax:
                xmax = point[0]
    
    xmax = xmax + ZOOM_ADDEND
    xmin = xmin - ZOOM_ADDEND
    
    #Array to store solutions
    solution_points = []
    
    #Create blank 3D plot
    fig = plt.figure()
    fig2 = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    front_ax = fig2.add_subplot(111)
    
    
    #Loop from min x to max x
    for i in np.arange(xmin, xmax, RES):
        
        new_dfe = sp.Subs(dfe, x, i)
        new_dfe = sp.simplify(new_dfe)
        
        #solve dfe = 0 given x
        solution = sp.nonlinsolve([new_dfe], [i, e])      
    
        
        for value in solution:
            #Filters out imaginary solutions
            if("I" in str(value[0]) or "I" in str(value[1])):
                continue
            else:
                #Variables
                xi = value[0]
                ei = value[1]
                
                dfxi = dfx.subs({x: xi.evalf(), e: ei.evalf()})
                y = dfxi.evalf()
                
                fi = f.subs({x: xi.evalf(), e: ei.evalf()})
                z = fi.evalf()
                
                #plot point
                ax.scatter(xi, y, z, c='black', marker='o')
                front_ax.scatter(xi, z, c='black', marker='o')
                
                #Console Test Output
                if VIEW_TEST_CODE == 1:
                    print('solution: ', solution)
                    solution_points.append(solution)
                    print('Value: ', value, type(value))
                    print('Value(0): ', xi, type(xi))
                    print('Value(1): ', ei, type(ei))

    
    #Displays all solutions
    if VIEW_TEST_CODE == 1:
        print('solution points:', solution_points, type(solution_points))
    
    #Set axis labels
    ax.set_xlabel('x')
    ax.set_ylabel('e')
    ax.set_zlabel('Z')
    
    front_ax.set_xlabel('x')
    front_ax.set_ylabel('Z')

    
    #Set axis ranges
    plt.xlim(int(xmin-2), int(xmax+2))
    plt.ylim(int(xmin-2), int(xmax+2))
    
    #Display plot
    plt.show()
    
    ######### Alternative Plot ##########
    #for point in solution_points:
    #    fig = go.Figure(data=[go.Scatter3d(x=point[0], y=point[1], z=point[2], mode='o')])
    #fig.show()
        
if __name__ == '__main__':
    main()
        