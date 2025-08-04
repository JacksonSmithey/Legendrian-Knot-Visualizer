# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 18:59:36 2024

@author: Jackson
"""
import numpy as np
import sympy as sp
import pandas as pd

def LPG(form):
    
    #DEMO FORM INPUT
    #form = {"eDim":1, "aDim":0, "genFam":"", "pThree":False, "pTop":False, "pFront":False, "granularity":1}
    #form["eDim"] = 2
    #form["aDim"] = 0
    #form["genFam"] = "(4-x**2)*e1-e1**3"
    #Trefoil
    #form["genFam"] = "(1/5)*e2**5+(1/3)*((e1-0)**2+(((x**2+4)*(x**2-16))/16))*e2**3+((e1-((1/16)*(x+3)*x*(x-3)))**2-0.5)*e2+((e1+((1/16)*(x+3)*x*(x-3)))**2-0.5)"
    #form["pThree"] = True
    #form["pTop"] = True
    #form["pFront"] = True
    #form["granularity"] = .1
    print(form)

    #User input (up to 5 of each)
    dimE = int(form["eDim"][0])
    dimA = int(form["aDim"][0])

    aiList = []
    
    #Constants
    RES = float(form["granularity"][0])
    ZOOM_ADDEND = 5
    VIEW_TEST_CODE = 1
    
    #Declare symbolic variables
    e1, e2, e3, e4, e5 = sp.symbols('e1 e2 e3 e4 e5', real = True)
    E = [e1, e2, e3, e4, e5]
    E = E[:dimE]
    a1, a2, a3, a4, a5 = sp.symbols('a1 a2 a3 a4 a5', real = True)
    A = [a1, a2, a3, a4, a5]
    A = A[:dimA] 
    genfam = form["genFam"][0]
    
    #Declare symbolic functions
    x = sp.Symbol('x', real=True)
    f = sp.Function('f')(x, tuple(E))
    f = sp.parse_expr(genfam, local_dict={ 'x':x
                                                ,'e1':e1,'e2':e2,'e3':e3,'e4':e4,'e5':e5
                                                ,'a1':a1,'a2':a2,'a3':a3,'a4':a4,'a5':a5})    
    f = sp.simplify(f)   
    
    #Calculate dfe
    DFE = []
    for e in E:
        DFE.append(sp.diff(f,e))

    #Calculate dfx
    dfx = sp.diff(f,x)

    #Solve for gradient(f) = 0
    GRAD_F = [dfx]
    for i in range(dimE):
        GRAD_F.append(DFE[i])
    match dimE:
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
    
    #Array to store solutions
    solution_points = []

    #init lists for point coords
    x_list = []
    y_list = []
    z_list = []

    #Loop from min x to max x
    for i in np.arange(xmin, xmax, RES):
        NEW_DFE = []
        for eqn in DFE:
            NEW_DFE.append(sp.simplify(sp.Subs(eqn, x, i)))

        #solve dfe = 0 given x
        E.insert(0, i) #nonlinsolve requires list input
        solution = sp.nonlinsolve(NEW_DFE, E)
        E.pop(0)

        for value in solution:                
            #Catch and skip imaginary solutions
            flag = False
            for toople in value:
                #toople = toople.subs({a1:ai1, a2:ai2, a3:ai3, a4:ai4, a5:ai5})
                if('I' in str(toople)):
                    flag = True
                    break
            if flag:
                break

            #Assign a_i Values       
            ai1 = 1
            ai2 = 1
            ai3 = 1
            ai4 = 1
            ai5 = 1
            if dimA >= 1:
                ai1 = aiList[0]
            if dimA >= 2:
                ai2 = aiList[1]
            if dimA >= 3:
                ai3 = aiList[2]
            if dimA >= 4:
                ai4 = aiList[3]
            if dimA >= 5:
                ai5 = aiList[4]
                
            #Assigns e_i values and substitutes a_i values
            xi = value[0]
            ei1 = value[1]
            ei1 = ei1.subs({a1:ai1, a2:ai2, a3:ai3, a4:ai4, a5:ai5})
            ei2 = 1
            ei3 = 1
            ei4 = 1
            ei5 = 1
            if dimE >= 2:
                ei2 = value[2]
                ei2 = ei2.subs({a1:ai1, a2:ai2, a3:ai3, a4:ai4, a5:ai5})
            if dimE >= 3:
                ei3 = value[3]
                ei3 = ei3.subs({a1:ai1, a2:ai2, a3:ai3, a4:ai4, a5:ai5})
            if dimE >= 4:
                ei4 = value[4]
                ei4 = ei4.subs({a1:ai1, a2:ai2, a3:ai3, a4:ai4, a5:ai5})
            if dimE >= 5:
                ei5 = value[5]
                ei5 = ei5.subs({a1:ai1, a2:ai2, a3:ai3, a4:ai4, a5:ai5})
            
            #substitute e_i and a_i values into dfx and f(x, e_i) for y,z coords    
            dfxi = dfx.subs({x:xi, e1:ei1, e2:ei2, e3:ei3, e4:ei4, e5:ei5,
                                   a1:ai1, a2:ai2, a3:ai3, a4:ai4, a5:ai5})
            y = dfxi.evalf()
            fi = f.subs({x:xi, e1:ei1, e2:ei2, e3:ei3, e4:ei4, e5:ei5,
                               a1:ai1, a2:ai2, a3:ai3, a4:ai4, a5:ai5})
            z = fi.evalf()
            x_list.append(str(xi))
            y_list.append(str(y))
            z_list.append(str(z))
            solution_points.append(solution)
                
            #Console Test Output
            if VIEW_TEST_CODE == 1:
                print('solution: ', solution)
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
    if VIEW_TEST_CODE == 1:
        print('solution points:', solution_points, type(solution_points))
        print('num e:', dimE)
        print('num a:', dimA)
        print('aiList:', aiList, type(aiList))
        print('E: ', E, type(E))
        print('A: ', A, type(A))
        print('f:', f, type(f))
        print('DFE:', DFE, type(DFE))
        print('zerograd:', zerograd, type(zerograd)) 
        print('min_x:', xmin, type(xmin))
        print('max_x:', xmax, type(xmax))
    
    #Create and return data frame
    data_frame = pd.DataFrame({
                    'x': x_list,
                    'y': y_list,
                    'z': z_list
                })
    return data_frame
    
if __name__ == '__main__':
    LPG()
        