# -*- coding: utf-8 -*-

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def main():
    
    #User input
    #num_a = 0
    num_e = 2
    
    
    #Declare symbolic variables
    #a = sp.symbols('a:{}'.format(num_a))
    e = sp.symbols('e:{}'.format(num_e))
    x = sp.Symbol('x')
    
    
    #Declare symbolic functions
    f = sp.Function('f')(x,e)
    f = -1/3*e[0]**3 + (4-(x+2)**2)*e[0] -1/3*e[1]**3 + (4-x**2)*e[1]
    
    
    #Calculate dfe, dfx, gradient(f)
    dfe = sp.diff(f,e)
    dfx = sp.diff(f,x)
    grad_f = [dfx, dfe]
    #gradient returned as a numerical list
    
    print('grad f', grad_f, type(grad_f))
    
    
    #Solve for gradient(f) = 0
    zerograd = sp.solve(grad_f, x, e)
    print('zerograd', type(zerograd), zerograd)
    
    #Store x values from gradient(f) = 0
    #xdata = zerograd.x
    xmin = min(zerograd, key=lambda pair: pair[0])[0] - 3
    xmax = max(zerograd, key=lambda pair: pair[0])[0] + 3

    print(xmin,' ', xmax)
    
    #To catch solutions for plotting
    solution_points = []
    
    #Loop from min x to max x
    for i in np.arange(xmin, xmax, 0.01):
        
        new_dfe = sp.Subs(dfe, x, i)
        print('new_dfe', type(new_dfe), new_dfe)
        
        #solve dfe = 0 given x
        solution = sp.nonlinsolve(new_dfe, [i, e])
        print('solution: ', solution)
        
        # Extract the solutions
        #sol_x = np.solution[x]
        #sol_e = float(solution[e])
        #solution_points.append((sol_x, dfx(sol_x,sol_e), f(sol_x,sol_e)))

    # Print the solutions
    #print(f"Solution: x = {sol_x}, y = dfx(sol_x), z = {1}")

    # Convert solution points to a NumPy array
    solution_points = np.array(solution_points)

    # Create a 3D scatter plot
    fig = plt.figure(projection='3d')

    # Plot the solution point
    fig.scatter(solution_points[:, 0], solution_points[:, 1], solution_points[:, 2], color='r', s=100, label='Solution Point')

    #plot point (x at dfe=0, dfx at dfe=0, f at dfe=0)
    plt.show()
        
if __name__ == '__main__':
    main()
        