# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 18:59:36 2024

@author: Jackson
"""

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import UId as UI

#TODO:
#       Support a values
#       Support subfunction inputs
#       Reeb Chords

def main():
    
    #UI
    inputList = UI.getData()
    print('inputList', inputList)
    
    #User input (up to 5 of each)
    num_e = inputList[0]
    num_a = inputList[1]
    num_s = inputList[3]
    threeDProj = inputList[4]
    topProj = inputList[5]
    frontProj = inputList[6]
    aiList = [4, 1, 2, 3 , 4]
    print('num e:', num_e)
    print('num a:', num_a)
    print('num s:', num_s)
    #print('aiList:', aiList, type(aiList))
    
    #constants
    RES = 0.1
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
    #f = sp.sympify(inputList[2])
    f = sp.parse_expr(inputList[2], local_dict={ 'x':x
                                                ,'e1':e1,'e2':e2,'e3':e3,'e4':e4,'e5':e5
                                                ,'a1':a1,'a2':a2,'a3':a3,'a4':a4,'a5':a5})
    print('f: ', f, type(f))
    print('genFAM:', inputList[2], type(inputList[2]))
    
    #One E-Dimension Example Functions
    #f = (4-x**2)*e1 - e1**3
    #f = (-1/3*e1**3 + (4 - x**2)*(e1+1))
    #Two E-Dimension Example Functions
    #f = (-1/3*e1**3 + (4 - x**2)*e1) + (4-x**2)*e2 - e2**3
    #f = -1/3*e1**3 +(4-x**2)*e1 -1/3*e2**3 + (4-(x+1)**2)*e2
    """ Trefoil
    f = (1/5)*e1**5 + (1/3)*e2**2*e1**3 + (1/48)*x**4*e1**3 - (1/4)*x**2*e1**3 
    - (4/3)*e1**3 + (9/8)*x*e2*e1 - (9/128)*x**4*e1 + (81/256)*x**2*e1 
    + (1/256)*x**6*e1 - (1/8)*x**3*e2*e1 + e2**2*e1 - 0.5*e1   - (9/8)*x*e2 
    - (9/128)*x**4 + (81/256)*x**2 + (1/256)*x**6+ (1/8)*x**3*e2 + e2**2 - 0.5 """
    #Three E-Dimension Example Functions
    #f = -1/3*e1**3 +(4-x**2)*e1 -1/3*e2**3 + (4-(x+1)**2)*e2 -1/3*e3**3 + (4-(x+2)**2)*e3
    #Four E-Dimension Example Functions
    #f = -1/3*e1**3 +(4-x**2)*e1 -1/3*e2**3 + (4-(x+1)**2)*e2 -1/3*e3**3 + (4-(x+2)**2)*e3 -1/3*e4**3 + (4-(x+3)**2)*e4
    #Five E-Dimension Example Functions
    #f = -1/3*e1**3 +(4-x**2)*e1 -1/3*e2**3 + (4-(x+1)**2)*e2 -1/3*e3**3 + (4-(x+2)**2)*e3 -1/3*e4**3 + (4-(x+3)**2)*e4 -1/3*e5**3 + (4-(x+4)**2)*e5
    
    
    f = sp.simplify(f)
    print('E: ', E, type(E))
    print('A: ', A, type(A))
    print('f:', f, type(f))    
    
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
    match num_e:
        case 1:
            zerograd = sp.solve(GRAD_F, x, e1)
        case 2:
            zerograd = sp.solve(GRAD_F, x, e1, e2)
        case 3:
            zerograd = sp.solve(GRAD_F, x, e1, e2, e3)
        case 4:
            zerograd = sp.solve(GRAD_F, x, e1, e2, e3, e4)
        case 5:
            zerograd = sp.solve(GRAD_F, x, e1, e2, e3, e4, e5)
    
    if VIEW_TEST_CODE == 1:
        print('DFE:', DFE, type(DFE))
        print('dfx:', dfx, type(dfx))
        print('GRAD_F', GRAD_F, type(GRAD_F))
        print('zerograd:', zerograd, type(zerograd))
    #Find min and max of 0 gradient points
    xmin = float('inf')
    xmax = float('-inf')
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
    
    #Create blank 3D plots
    if threeDProj:
        fig = plt.figure()
        ax = fig.add_subplot(311, projection='3d')
    if frontProj:
        fig2 = plt.figure()
        front_ax = fig2.add_subplot(312)
    if topProj:
        fig3 = plt.figure()
        top_ax = fig3.add_subplot(313)    

    #Loop from min x to max x
    for i in np.arange(xmin, xmax, RES):
        NEW_DFE = []
        for eqn in DFE:
            NEW_DFE.append(sp.simplify(sp.Subs(eqn, x, i)))

        #solve dfe = 0 given x
        E.insert(0, i)
        solution = sp.nonlinsolve(NEW_DFE, E)
        E.pop(0)
    
        for value in solution:       
            ai1 = 1
            ai2 = 1
            ai3 = 1
            ai4 = 1
            ai5 = 1
            if num_a >= 1:
                ai1 = aiList[0]
            if num_a >= 2:
                ai2 = aiList[1]
            if num_a >= 3:
                ai3 = aiList[2]
            if num_a >= 4:
                ai4 = aiList[3]
            if num_a >= 5:
                ai5 = aiList[4]
                
            flag = False
            for toople in value:
                toople = toople.subs({a1:ai1, a2:ai2, a3:ai3, a4:ai4, a5:ai5})
                print('tooop',toople)
                if('I' in str(toople)):
                    flag = True
                    break
            if flag:
                break
                
            xi = value[0]
            ei1 = value[1]
            ei1 = ei1.subs({a1:ai1, a2:ai2, a3:ai3, a4:ai4, a5:ai5})
            ei2 = 1
            ei3 = 1
            ei4 = 1
            ei5 = 1
            if num_e >= 2:
                ei2 = value[2]
                ei2 = ei2.subs({a1:ai1, a2:ai2, a3:ai3, a4:ai4, a5:ai5})
            if num_e >= 3:
                ei3 = value[3]
                ei3 = ei3.subs({a1:ai1, a2:ai2, a3:ai3, a4:ai4, a5:ai5})
            if num_e >= 4:
                ei4 = value[4]
                ei4 = ei4.subs({a1:ai1, a2:ai2, a3:ai3, a4:ai4, a5:ai5})
            if num_e >= 5:
                ei5 = value[5]
                ei5 = ei5.subs({a1:ai1, a2:ai2, a3:ai3, a4:ai4, a5:ai5})
            
                
            dfxi = dfx.subs({x:xi, e1:ei1, e2:ei2, e3:ei3, e4:ei4, e5:ei5,
                                   a1:ai1, a2:ai2, a3:ai3, a4:ai4, a5:ai5})
            y = dfxi.evalf()
            fi = f.subs({x:xi, e1:ei1, e2:ei2, e3:ei3, e4:ei4, e5:ei5,
                               a1:ai1, a2:ai2, a3:ai3, a4:ai4, a5:ai5})
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
            if threeDProj:
                ax.scatter(xi, y, z, c='black', marker='o')
            if frontProj:
                front_ax.scatter(xi, z, c='black', marker='o')
            if topProj:
                top_ax.scatter(xi, y, c='black', marker='o')

    
    #Displays all solutions
    if VIEW_TEST_CODE == 1:
        print('solution points:', solution_points, type(solution_points))
    
    #Set axis labels
    if threeDProj:
        ax.set_xlabel('x')
        ax.set_ylabel('e')
        ax.set_zlabel('Z')
    if frontProj:
        front_ax.set_xlabel('x')
        front_ax.set_ylabel('Z')
        #if reebChord:
        #    front_ax.axvline(xValue, color='r') //VERTICAL
        #    front_ax.axhline(xValue, color='green') //HORIZONTAL
    if topProj:
        top_ax.set_xlabel('x')
        top_ax.set_ylabel('e')
        #if reebChord:
        #    front_ax.axvline(xValue, color='r') //VERTICAL
        #    front_ax.axhline(xValue, color='green') //HORIZONTAL
    
    #Set axis ranges
    plt.xlim(int(xmin-2), int(xmax+2))
    plt.ylim(int(xmin-2), int(xmax+2))
    
    #Display plot
    plt.show()
    
if __name__ == '__main__':
    main()
        