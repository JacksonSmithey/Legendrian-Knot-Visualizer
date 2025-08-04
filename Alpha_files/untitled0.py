# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 18:59:36 2024

@author: Jackson
"""

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
    
    #User input (up to 5 of each)
    num_a = 0
    num_e = 4
    
    #constants
    RES = 0.1  #FIXME: Nonlinsolve doesn't appreciate RES = 1
    ZOOM_ADDEND = 5
    VIEW_TEST_CODE = 1
    
    #Declare symbolic variables
    e1, e2, e3, e4, e5 = sp.symbols('e1 e2 e3 e4 e5', real = True)
    E = [e1, e2, e3, e4, e5]
    E = E[:num_e]
    a1, a2, a3, a4, a5 = sp.symbols('a1 a2 a3 a4 a5', real = True)
    A = [a1, a2, a3, a4, a5]
    A = A[:num_a] 
    x = sp.Symbol('x', real=True)
    
    #Declare symbolic functions
    f = sp.Function('f')(x, tuple(E))
    
    #One E-Dimension Example Functions
    #f = (4-x**2)*e1 - e1**3
    #f = (-1/3*e1**3 + (4 - x**2)*(e1+1))
    
    #Two E-Dimension Example Functions
    #f = (-1/3*e1**3 + (4 - x**2)*e1) + (4-x**2)*e2 - e2**3
    #f = -1/3*e1**3 +(4-x**2)*e1 -1/3*e2**3 + (4-(x+1)**2)*e2
    """ Trefoil
    f = ((1/5)*v^5 + (1/3)*u^2*v^3 + (1/48)*x^4*v^3 - (1/4)*x^2*v^3 
    - (4/3)*v^3 + (9/8)*x*u*v - (9/128)*x^4*v + (81/256)*x^2*v
    + (1/256)*x^6*v - (1/8)*x^3*u*v + u^2*v - 0.5*v
    - (9/8)*x*u - (9/128)*x^4 + (81/256)*x^2 + (1/256)*x^6
    + (1/8)*x^3*u + u^2 - 0.5
    """
    
    #Three E-Dimension Example Functions
    #f = -1/3*e1**3 +(4-x**2)*e1 -1/3*e2**3 + (4-(x+1)**2)*e2 -1/3*e3**3 + (4-(x+2)**2)*e3
    
    #Four E-Dimension Example Functions
    f = -1/3*e1**3 +(4-x**2)*e1 -1/3*e2**3 + (4-(x+1)**2)*e2 -1/3*e3**3 + (4-(x+2)**2)*e3 -1/3*e4**3 + (4-(x+3)**2)*e4
    
    
    #Five E-Dimension Example Functions
    #f = -1/3*e1**3 +(4-x**2)*e1 -1/3*e2**3 + (4-(x+1)**2)*e2 -1/3*e3**3 + (4-(x+2)**2)*e3 -1/3*e4**3 + (4-(x+3)**2)*e4 -1/3*e5**3 + (4-(x+4)**2)*e5
    
    
    
    f = sp.simplify(f)
    print('E: ', E, type(E))
    print('f:', f)
    
    
    #Calculate dfe
    DFE = []
    for e in E:
        DFE.append(sp.diff(f,e))
    #Calculate dfx
    dfx = sp.diff(f,x)
        
    #Solve for gradient(f) = 0
    GRAD_F = [dfx]
    for i in range(num_e):
        GRAD_F.append(DFE[i])
    zerograd = sp.solve(GRAD_F, x, e1, e2)
    
    
    
    xmin = 0
    xmax = 0
    xmin = 0
    
    if VIEW_TEST_CODE == 1:
        print('DFE:', DFE, type(DFE))
        print('dfx:', dfx, type(dfx))
        print('GRAD_F', GRAD_F, type(GRAD_F))
        print('zerograd:', zerograd, type(zerograd))
    #Find min and max of 0 gradient points
    for point in zerograd:        
        if isinstance(point[0], sp.Float) or isinstance(point[0], sp.Integer):
            if point[0] < xmin:
                xmin = point[0]
            if point[0] > xmax:
                xmax = point[0]
    
    xmax = xmax + ZOOM_ADDEND
    xmin = xmin - ZOOM_ADDEND
    
    if VIEW_TEST_CODE == 1:
        print('min_x:', xmin, type(xmin))
        print('max_x:', xmax, type(xmax))
    
    #Array to store solutions
    solution_points = []
    
    #Create blank 3D plot
    fig = plt.figure()
    fig2 = plt.figure()
    fig3 = plt.figure()
    ax = fig.add_subplot(311, projection='3d')
    front_ax = fig2.add_subplot(312)
    top_ax = fig3.add_subplot(313)
    
    
    #Loop from min x to max x
    for i in np.arange(xmin, xmax, RES):
        NEW_DFE = []
        for eqn in DFE:
            NEW_DFE.append(sp.simplify(sp.Subs(eqn, x, i)))
        
        #new_dfe = sp.simplify(new_dfe)

        #solve dfe = 0 given x
        E.insert(0, i)
        solution = sp.nonlinsolve(NEW_DFE, E)
        E.pop(0)
    
        for value in solution:
            match num_e:
                case 1:
                    if("I" in str(value[0]) or "I" in str(value[1])):
                        break
                    else:
                        xi = value[0]
                        ei1 = value[1]
                        dfxi = dfx.subs({x: xi, e1: ei1})
                        y = dfxi.evalf()
                        fi = f.subs({x: xi, e1: ei1})
                        
                        z = fi.evalf()
                        
                        #Console Test Output
                        if VIEW_TEST_CODE == 1:
                            print('solution: ', solution)
                            solution_points.append(solution)
                            print('Value: ', value, type(value))
                            print('xi: ', xi, type(xi))
                            print('dfxi: ', dfxi, type(dfxi))
                            print('y: ', y, type(y))
                            print('fi: ', fi, type(fi))
                            print('z', z, type(z))

                        #plot point
                        ax.scatter(xi, y, z, c='black', marker='o')
                        front_ax.scatter(xi, z, c='black', marker='o')
                        top_ax.scatter(xi, y, c='black', marker='o')
                        
                case 2:
                    if("I" in str(value[0]) or "I" in str(value[1])
                       or "I" in str(value[2]) or "e1" in str(value[1])
                          or "e2" in str(value[2])):
                        continue
                    else:
                        xi = value[0]
                        ei1 = value[1]
                        ei2 = value[2]
                        

                        dfxi = dfx.subs({x: xi, e1: ei1, e2: ei2})
                        y = dfxi.evalf()
                        fi = f.subs({x: xi, e1: ei1, e2: ei2})
                        z = fi.evalf()
                        
                        #Console Test Output
                        if VIEW_TEST_CODE == 1:
                            print('solution: ', solution)
                            solution_points.append(solution)
                            print('Value: ', value, type(value))
                            print('xi: ', xi, type(xi))
                            print('ei1: ', ei1, type(ei1))
                            print('ei2: ', ei2, type(ei2))
                            print('dfxi: ', dfxi, type(dfxi))
                            print('y: ', y, type(y))
                            print('fi: ', fi, type(fi))
                            print('z', z, type(z))
                        #plot point
                        ax.scatter(xi, y, z, c='black', marker='o')
                        front_ax.scatter(xi, z, c='black', marker='o')
                        top_ax.scatter(xi, y, c='black', marker='o')
                        
                case 3:
                    if("I" in str(value[0]) or "I" in str(value[1])
                       or "I" in str(value[2]) or "I" in str(value[3]) 
                       or "e1" in str(value[1]) or "e2" in str(value[2])
                       or "e3" in str(value[3])):
                        continue
                    else:
                        xi = value[0]
                        ei1 = value[1]
                        ei2 = value[2]
                        ei3 = value[3]
                        
                        dfxi = dfx.subs({x: xi, e1: ei1, e2: ei2, e3: ei3})
                        y = dfxi.evalf()
                        fi = f.subs({x: xi, e1: ei1, e2: ei2, e3: ei3})
                        z = fi.evalf()
                        
                        #Console Test Output
                        if VIEW_TEST_CODE == 1:
                            print('solution: ', solution)
                            solution_points.append(solution)
                            print('Value: ', value, type(value))
                            print('xi: ', xi, type(xi))
                            print('ei1: ', ei1, type(ei1))
                            print('ei2: ', ei2, type(ei2))
                            print('ei3: ', ei3, type(ei3))
                            print('dfxi: ', dfxi, type(dfxi))
                            print('y: ', y, type(y))
                            print('fi: ', fi, type(fi))
                            print('z', z, type(z))
                        #plot point
                        ax.scatter(xi, y, z, c='black', marker='o')
                        front_ax.scatter(xi, z, c='black', marker='o')
                        top_ax.scatter(xi, y, c='black', marker='o')
                case 4:
                    if("I" in str(value[0]) or "I" in str(value[1])
                       or "I" in str(value[2]) or "I" in str(value[3]) 
                       or "I" in str(value[4]) or "e1" in str(value[1]) 
                       or "e2" in str(value[2]) or "e3" in str(value[3])
                       or "e4" in str(value[4])):
                        continue
                    else:
                        xi = value[0]
                        ei1 = value[1]
                        ei2 = value[2]
                        ei3 = value[3]
                        ei4 = value[4]
                        
                        dfxi = dfx.subs({x: xi, e1: ei1, e2: ei2, e3: ei3, e4: ei4})
                        y = dfxi.evalf()
                        fi = f.subs({x: xi, e1: ei1, e2: ei2, e3: ei3, e4: ei4})
                        z = fi.evalf()
                        
                        #Console Test Output
                        if VIEW_TEST_CODE == 1:
                            print('solution: ', solution)
                            solution_points.append(solution)
                            print('Value: ', value, type(value))
                            print('xi: ', xi, type(xi))
                            print('ei1: ', ei1, type(ei1))
                            print('ei2: ', ei2, type(ei2))
                            print('ei3: ', ei3, type(ei3))
                            print('ei4: ', ei4, type(ei4))
                            print('dfxi: ', dfxi, type(dfxi))
                            print('y: ', y, type(y))
                            print('fi: ', fi, type(fi))
                            print('z', z, type(z))
                        #plot point
                        ax.scatter(xi, y, z, c='black', marker='o')
                        front_ax.scatter(xi, z, c='black', marker='o')
                        top_ax.scatter(xi, y, c='black', marker='o')
                case 5:
                    if("I" in str(value[0]) or "I" in str(value[1])
                       or "I" in str(value[2]) or "I" in str(value[3]) 
                       or "I" in str(value[4]) or "I" in str(value[5])
                       or "e1" in str(value[1]) or "e2" in str(value[2])
                       or "e3" in str(value[3]) or "e4" in str(value[4])
                       or "e5" in str(value[5])):
                        continue
                    else:
                        xi = value[0]
                        ei1 = value[1]
                        ei2 = value[2]
                        ei3 = value[3]
                        ei4 = value[4]
                        ei5 = value[5]
                        
                        dfxi = dfx.subs({x: xi, e1: ei1, e2: ei2, e3: ei3, e4: ei4, e5: ei5})
                        y = dfxi.evalf()
                        fi = f.subs({x: xi, e1: ei1, e2: ei2, e3: ei3, e4: ei4, e5: ei5})
                        z = fi.evalf()
                        
                        #Console Test Output
                        if VIEW_TEST_CODE == 1:
                            print('solution: ', solution)
                            solution_points.append(solution)
                            print('Value: ', value, type(value))
                            print('xi: ', xi, type(xi))
                            print('ei1: ', ei1, type(ei1))
                            print('ei2: ', ei2, type(ei2))
                            print('ei3: ', ei3, type(ei3))
                            print('ei4: ', ei4, type(ei4))
                            print('ei5: ', ei5, type(ei5))
                            print('dfxi: ', dfxi, type(dfxi))
                            print('y: ', y, type(y))
                            print('fi: ', fi, type(fi))
                            print('z', z, type(z))
                        #plot point
                        ax.scatter(xi, y, z, c='black', marker='o')
                        front_ax.scatter(xi, z, c='black', marker='o')
                        top_ax.scatter(xi, y, c='black', marker='o')

                
                    #Console Test Output
                    if VIEW_TEST_CODE == 1:
                        print('solution: ', solution)
                        solution_points.append(solution)
                        print('Value: ', value, type(value))
                        print('Value(0): ', xi, type(xi))
                        #print('Value(1): ', ei, type(ei))
    
    #Displays all solutions
    if VIEW_TEST_CODE == 1:
        print('solution points:', solution_points, type(solution_points))
    
    #Set axis labels
    ax.set_xlabel('x')
    ax.set_ylabel('e')
    ax.set_zlabel('Z')
    
    front_ax.set_xlabel('x')
    front_ax.set_ylabel('Z')
    
    top_ax.set_xlabel('x')
    top_ax.set_ylabel('e')
    
    #Set axis ranges
    plt.xlim(int(xmin-2), int(xmax+2))
    plt.ylim(int(xmin-2), int(xmax+2))
    
    #Display plot
    plt.show()
    
if __name__ == '__main__':
    main()
        