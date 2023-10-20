# arr = [0,1,2,3,4,5,6,7,8,9]


# for i in range(4):
#     print(i)

# for i in range(5, 10):
#     print(i)

import random

def QuickSelect(arr):
    if len(arr) == 0:
        return None
    # Your code here
    below = []
    above = []
    k = 5
    for j in range(k):
        if j == k:
            break
        if arr[j][0] <= arr[k][0]:
            below.append(arr[j])
        if arr[j][0] >  arr[k][0]:
            above.append(arr[j])
    if len(below) == i:
        return arr[k]
    elif len(below) < i:
        return QuickSelect(above, i - len(below) - 1)
    else:
        return QuickSelect(below, i)

k = range(10) + range(20)
print(k)