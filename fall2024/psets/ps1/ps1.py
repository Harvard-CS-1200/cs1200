from asyncio import base_tasks
import math
import time
import random

"""
See below for mergeSort and singletonBucketSort functions, and for the BC helper function.
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

def singletonBucketSort(univsize, arr):
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

def radixSort(univsize, base, arr):
    # Find number of digits needed
    k = math.ceil(math.log(univsize) / math.log(base)) 

    # Break each key into subkeys using BC
    for i in range(len(arr)):
        key, value = arr[i]
        arr[i] = (BC(key, base, k), value) 
    
    # Sort by each digit, starting from LSD
    for digit_index in range(k):
        arr = singletonBucketSort(base, [(elt[0][digit_index], elt[1]) for elt in arr])

    # Reconstruct original keys from the sorted digit arrays
    for i in range(len(arr)):
        digits, value = arr[i]
        key = sum(d * (base ** idx) for idx, d in enumerate(digits))  
        arr[i] = (key, value)
    
    return arr
