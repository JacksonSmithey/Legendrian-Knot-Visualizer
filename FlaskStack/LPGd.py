# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 18:59:36 2024

@author: Jackson
"""
import numpy as np
import sympy as sp
import pandas as pd
from itertools import combinations
import html
import re

def LPG(form):

    def Validate(form):
        for input in form:
            input = html.escape(input)
            input = re.sub(r'[^a-zA-Z0-9+\-*\/\(\)\s]', '', input)
        if int(form["eDim"][0]) not in range(1, 6):
            raise ValueError("E-Dimension must be in the range [1,5]")
        if len(form["aList"])//3 not in range(0, 21):
            raise ValueError("A-Variable count may not exceed 20")
        if len(form["genFam"]) not in range(0, 800):
            raise ValueError("Genfam contains too many characters. To bypass, edit LPGd.py Validation().")
        if float(form["granularity"][0]) < .0005:
            raise ValueError("Granularity has a minimum value of .0005")
    try:
        Validate(form)
    except ValueError as e:
        print(f"Error: {e}")
        return
    
    #DEMO FORM INPUT
    #form["eDim"] = 1
    #form["aList"] = {0, 1, 1, 1, 1.5, 0.5} #{a1_start, a1_stop, a1_increment, a2_start, a2_stop, a2_increment}       
    #form["genFam"] = "(4-x**2)*e1-e1**3"
    #form["pThree"] = True
    #form["pTop"] = True
    #form["pFront"] = True
    #form["granularity"] = .1
    print(form)

    #Rename commonly used vars
    dimE = int(form["eDim"][0])
    dimA = int(len(form["aList"]) // 3)
    genfam = str(form["genFam"][0])
    aList = form["aList"]
    print('dimA', dimA)
    
    #Constants
    RES = float(form["granularity"][0])
    ZOOM_ADDEND = 5
    VIEW_TEST_CODE = 1

    #Generate combinations of a_i values
    ai_array = []
    for i in range(0, dimA):
        ai_vals = []
        ai_start = float(form["aList"][3*i])
        ai_stop = float(form["aList"][3*i + 1])
        ai_increment = float(form["aList"][3*i + 2])
        while ai_start <= ai_stop:
            ai_vals.append(ai_start)
            ai_start += ai_increment
        ai_array.append(ai_vals)
    for ai_row in ai_array:
        ai_vals.append(combinations(ai_array))
    for p in ai_vals:
        print(p)

    
    #Declare symbolic variables and functions
    e1, e2, e3, e4, e5 = sp.symbols('e1 e2 e3 e4 e5', real = True)
    E = [e1, e2, e3, e4, e5] ; E = E[:dimE]
    a1, a2, a3, a4, a5 = sp.symbols('a1 a2 a3 a4 a5', real = True)
    A = [a1, a2, a3, a4, a5] ; A = A[:dimA] 

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

    #Solve grad(f)=0 to find bounds for x
    GRAD_F = [dfx]
    for i in range(dimE):
        GRAD_F.append(DFE[i])
    match dimE:
        case 1: zerograd = sp.solve(GRAD_F, x, e1)
        case 2: zerograd = sp.solve(GRAD_F, x, e1, e2)
        case 3: zerograd = sp.solve(GRAD_F, x, e1, e2, e3)
        case 4: zerograd = sp.solve(GRAD_F, x, e1, e2, e3, e4)
        case 5: zerograd = sp.solve(GRAD_F, x, e1, e2, e3, e4, e5)

    #Loop over all combinations of a_i values
    for k in range(ai_vals.shape[0]):
        print('k:', k)
        ais = ai_vals
    
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
                    if('I' in str(toople)):
                        flag = True
                        break
                if flag:
                    break
                    
                #Assign e_i values and substitute a_i values
                xi = value[0]
                eis = {"e1":1, "e2":1, "e3":1, "e4":1, "e5":1}
                for i in range(1, dimE):
                    eis[f"e{i}"] = value[i]
                
                #substitute e_i and a_i values into dfx and f(x, e_i) for y,z coords    
                dfxi = dfx.subs({x:xi, **eis, **ais})
                y = dfxi.evalf()
                fi = f.subs({x:xi, **eis, **ais})
                z = fi.evalf()
                x_list.append(str(xi))
                y_list.append(str(y))
                z_list.append(str(z))
                solution_points.append(solution)
                    
                #Console Test Output
                if VIEW_TEST_CODE == 1:
                    print('solution: ', solution)
                    print('Value: ', value, type(value))
                    print('a start,stop,increment:', aList[i]["start"])
                    print('xi: ', xi, type(xi))
                    print('eis: ', eis, type(eis))
                    print('dfxi: ', dfxi, type(dfxi))
                    print('y: ', y, type(y))
                    print('fi: ', fi, type(fi))
                    print('z', z, type(z))
    if VIEW_TEST_CODE == 1:
        print('solution points:', solution_points, type(solution_points))
        print('num e:', dimE)
        print('num a:', dimA)
        print('aList:', aList, type(aList))
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
        