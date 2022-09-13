from asyncio import base_tasks
from cmath import log
from itertools import count
import math
import time
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

def radixSort(U, b, arr):
    n = len(arr)
    k = math.ceil((log(U)/log(b)).real)
    V_prime = []
    for elt in arr:
        V_prime.append(BC(elt[0], b, k))
    new_arr = [[x, [y, v]] for [x, y], v in zip(arr, V_prime)]
    for i in range(k):
        for j in range(n):
            new_arr[j][0] = new_arr[j][1][1][i]
        new_arr = countSort(b, new_arr)
    for i in range(n):
        k_i = 0
        for j in range(k):
            k_i += new_arr[i][1][1][j] * (b ** j)
        new_arr[i] = [k_i, new_arr[i][1][0]]
    return new_arr


count_sort = []
merge_sort = []
radix_sort = []
# print(radixSort(80, 10, [[50, 1], [60, 7], [10, 2], [20, 4], [30, 3], [80, 9], [70, 8], [90, 4], [10, 1], [10, 0]]))
# n_values = [2 ** i for i in range(17)]
# U_values = [2 ** i for i in range(21)]

for i in range(17):
    n = 2 ** i
    for j in range(21):
        U_value = 2 ** j
        array = [[random.randint(0, U_value - 1), 0] for _ in range(n)]
        start_one = time.time()
        countSort(U_value, array)
        end_one = time.time()
        count_sort.append([i, j, end_one - start_one])

        start_two = time.time()
        mergeSort(array)
        end_two = time.time()
        merge_sort.append([i, j, end_two - start_two])

        
        length = 2 if n < 2 else n
        start_three = time.time()
        radixSort(U_value, length, array)
        end_three = time.time()
        radix_sort.append([i, j, end_three - start_three])

count_win_x = []
count_win_y = []
merge_win_x = []
merge_win_y = []
radix_win_x = []
radix_win_y = []

for i in range(len(count_sort)):
    if min(count_sort[i][2], merge_sort[i][2], radix_sort[i][2]) == count_sort[i][2]:
        # plt.scatter(count_sort[i][1], count_sort[i][0], label='countSort', color='red')
        count_win_x.append(count_sort[i][1])
        count_win_y.append(count_sort[i][0])
    elif min(count_sort[i][2], merge_sort[i][2], radix_sort[i][2]) == merge_sort[i][2]:
        # plt.scatter(merge_sort[i][1], merge_sort[i][0], label='mergeSort', color='blue')
        merge_win_x.append(merge_sort[i][1])
        merge_win_y.append(merge_sort[i][0])
    else:
        # plt.scatter(radix_sort[i][1], radix_sort[i][0], label='radixSort', color='green')
        radix_win_x.append(radix_sort[i][1])
        radix_win_y.append(radix_sort[i][0])

plt.scatter(count_win_x, count_win_y, color='red', label='countSort')
plt.scatter(merge_win_x, merge_win_y, color='blue', label='mergeSort')
plt.scatter(radix_win_x, radix_win_y, color='green', label='radixSort')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xlabel('log_U')
plt.ylabel('log_n')
plt.title('Fastest Algorithm for Arrays of size n + universe U')
plt.tight_layout()
plt.show()
