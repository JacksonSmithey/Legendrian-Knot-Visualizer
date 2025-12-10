from itertools import product

def Combinations(aList, dimA):
# aList: [a1_start, a1_stop, a1_increment, a2_start, a2_stop, a2_increment, ...]
# dimA: number of ai variables OR length of aList/3
#
# return: a list of dimA-length tuples 
#         each tuple is a unique combination of 1 of each ai value

    aiList = []
    aiTupleList = []

    # Generate sequences of ai values and store them in a list of lists
    for i in range(0, dimA):
        aiVals = []
        ai_start = float(aList[3*i])
        ai_stop = float(aList[3*i + 1])
        ai_increment = float(aList[3*i + 2])
        while ai_start <= ai_stop:
            aiVals.append(ai_start)
            ai_start += ai_increment
        aiList.append(aiVals)

    # Generate all combinations
    aiTupleList = list(product(*aiList))

    return aiTupleList