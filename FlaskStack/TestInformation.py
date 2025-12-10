

def SolutionInfo(solution, value, xi, eis, dfxi, y, fi, z):
    print('solution: ', solution)
    print('Value: ', value, type(value))
    print('xi: ', xi, type(xi))
    print('eis: ', eis, type(eis))
    print('dfxi: ', dfxi, type(dfxi))
    print('y: ', y, type(y))
    print('fi: ', fi, type(fi))
    print('z', z, type(z))

def SolutionSetInfo(solution_points, dimE, dimA, aList, E, A, f, DFE, zerograd, xmin, xmax):
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