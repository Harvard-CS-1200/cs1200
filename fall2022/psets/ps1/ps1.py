from asyncio import base_tasks
import math
import time
import random
import numpy as np
import matplotlib.pyplot as plt
import csv

"""
See below for mergeSort and countSort functions, and for a useful helper function.
In order to run your experiments, you may find the functions random.randint() and time.time() useful.

In general, for each value of n and each universe size 'U' you will want to
    1. Generate a random array of length n whose keys are in 0, ..., U - 1
    2. Run count sort, merge sort, and radix sort ~10 times each,
       averaging the runtimes of each function. 
       (If you are finding that your code is taking too long to run with 10 repitions, you should feel free to decrease that number)

To graph, you can use a library like matplotlib or simply put your data in a Google/Excel sheet.
A great resource for all your (current and future) graphing needs is the Python Graph Gallery 
"""


def merge(arr1, arr2):
    sortedArr = []

    i = 0
    j = 0
    while i < len(arr1) or j < len(arr2):
        if i >= len(arr1):
            sortedArr.append(arr2[j])
            j += 1
        elif j >= len(arr2):
            sortedArr.append(arr1[i])
            i += 1
        elif arr1[i][0] <= arr2[j][0]:
            sortedArr.append(arr1[i])
            i += 1
        else:
            sortedArr.append(arr2[j])
            j += 1

    return sortedArr

def mergeSort(arr):
    if len(arr) < 2:
        return arr

    midpt = int(math.ceil(len(arr)/2))

    half1 = mergeSort(arr[0:midpt])
    half2 = mergeSort(arr[midpt:])

    return merge(half1, half2)

def countSort(univsize, arr):
    universe = []
    for i in range(univsize):
        universe.append([])

    for elt in arr:
        universe[elt[0]].append(elt)

    sortedArr = []
    for lst in universe:
        for elt in lst:
            sortedArr.append(elt)

    return sortedArr

def BC(n, b, k):
    if b < 2:
        raise ValueError()
    digits = []
    for i in range(k):
        digits.append(n % b)
        n = n // b
    if n > 0:
        raise ValueError()
    return digits

# U - universe of keys
# b - base (natural number)
# A - array to be sorted
def radix_sort(U, b, A):
    start_rad = time.time()
    k = math.ceil(math.log(U)/math.log(b))

    # print(A, "\n")
    data_struct = []

    # create data struct of form: (OG key -- none at first, (OG value, [output list from BC]))
    for i in range(len(A)):
        data_struct.append((None, (A[i][1], BC(A[i][0], b, k))))

    # print(data_struct)

    for j in range(k):
        for i in range(len(A)):
            # replace tuple so that the key to be sorted with countSort 
            #    iterates through the digits from BC
            data_struct[i] = (data_struct[i][1][1][j], data_struct[i][1])
            
        # print("J", j, "\n", data_struct, "\n")
        data_struct = (countSort(b, data_struct))
        # print(data_struct, "\n")

    # print(data_struct, "\n")
    end_rad = time.time()

    return(data_struct)

# bloop = radix_sort(13, 2, [(4,'a'), (5,'b'), (1,'c'), (12,'d')])

# See below for mergeSort and countSort functions, and for a useful helper function.
# In order to run your experiments, you may find the functions random.randint() and time.time() useful.

# In general, for each value of n and each universe size 'U' you will want to
#     1. Generate a random array of length n whose keys are in 0, ..., U - 1
#     2. Run count sort, merge sort, and radix sort ~10 times each,
#        averaging the runtimes of each function. 
#        (If you are finding that your code is taking too long to run with 10 repitions, you should feel free to decrease that number)

# univsize = 50
univsize = int(2**16)
# nsize = 50
nsize = int(2**20)
radixTime=[]
countTime=[]
mergeTime=[]

graphRow=[]
graphArr=[]

U=[]
n_len=[]

for i in range(1,17):
    n_len.append(2**i)

for i in range(1,21):
    U.append(2**i)


def run_tests():
    # U = list[range(1,2^20)]
    # n = list(range(2,2^16)]
    
    

    with open('/Users/cpartridge/cs120/fall2022/psets/ps1/sortCompare.csv', 'w') as f:
        writer = csv.writer(f)
        for uni in U:
            # for every value of n, run 10 trials of each sorting algorithm each with a 
            #   different random array of length n with keys in 
            # radixRow=[]
            # countRow=[]
            # mergeRow=[]
            graphRow=[]
            # graphRow=np.ones(nsize)
            count = 0
            for n in n_len:
                count+=1
                print(uni,n)
            # 10 trials with the same inputs
                for i in range(2):
                    # generate random array of length n
                    r_Time = 0
                    m_Time = 0
                    c_Time = 0

                    rand_array = []
                    for x in range(n):
                        rand_array.append((random.randint(0,uni-1), " "))

                    before = time.time()
                    mergeSort(rand_array)
                    after = time.time()

                    m_Time += after - before

                    before = time.time()
                    countSort(uni, rand_array)
                    after = time.time()

                    c_Time += after - before

                    before = time.time()
                    radix_sort(uni, n, rand_array)
                    after = time.time()

                    r_Time += after - before


                # radixRow.append(r_Time/10)
                # mergeRow.append(m_Time/10)
                # countRow.append(c_Time/10)
                avgC_time = c_Time/2 #0
                avgR_time = r_Time/2 #1
                avgM_time = m_Time/2 #2
                min_time = min(avgC_time, avgM_time, avgR_time)
                if min_time == avgC_time:
                    # graphRow[count] = 0
                    graphRow.append(0)
                elif min_time == avgR_time:
                    # graphRow[count] = 1
                    graphRow.append(1)
                elif min_time == avgM_time:
                    # graphRow[count] = 2
                    graphRow.append(2)


            # radixTime.append(radixRow)
            # mergeTime.append(mergeRow)
            # countRow.append(countRow)
            graphArr.append(graphRow)
            # writer.writerow((uni, n, graphRow))

    # print(graphArr)
    return(graphArr) 


graphArr = run_tests()
print(graphArr)
# print(len(graphArr[0]))
uCount=0
nCount=0
with open('/Users/cpartridge/cs120/fall2022/psets/ps1/sortCompare.csv', 'w') as f:
    for uni in U:
        nCount=0
        for n in n_len:
            
            writer = csv.writer(f)
            # print("Counts", uCount, nCount)
            # print("indexers",uni,n)
            # print("grapharray",graphArr[uCount][nCount])
            # writer.writerows(radixTime)
            # print(uni,n)
            writer.writerow((uni, n, graphArr[uCount][nCount]))
            nCount+=1
            # writer.writerows(graphArr)

        uCount+=1









