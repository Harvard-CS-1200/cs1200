import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import time
import math
import random

random.seed(120)

#
# Make Sure to Read the README
#


####################
#                  #
# Your Code Here   #
#                  #
####################


'''
A Las Vegas Algorithm to find a key-value pair (Ij, Kj) such that Kj is an i’th smallest key.
arr: a list of key-value pair tuples
    e.g. [(K0, V0), (K1, V1), ..., (Ki, Vi), ..., (Kn, Vn)] 
    ... in this problem set, the values are irrelevant
i: an integer [0, n-1] 
returns: An key-value pair (Kj, Vj) such that Kj is an i’th smallest key.
'''


def QuickSelect(arr, i):
    # Your code here

    # Feel free to use get_random_index(arr) or get_random_int(start_inclusive, end_inclusive)
    # ... see the helper functions below
    pass
    return (0, -1)


'''
Uses MergeSort to resolve a number of queries where each query is to find an key-value pair (Kj, Vj) such that Kj is an i’th smallest key.
arr: a list of key-value pair tuples
    e.g. [(K0, V0), (K1, V1), ..., (Ki, Vi), ..., (Kn, Vn)] 
    ... in this problem set, the values are irrelevant
query_list (aka i_arr): a list of integers [0, n-1] 
returns: An list of key-value pairs such that for each query qi, the i'th element in the returned list is (Kj, Vj) such that Kj is an i’th smallest key.
NOTE: This is different from the QuickSelect definition. This function takes in a set of queries and returns a list corresponding to their results. 
    ... this is to properly benchmark for the experiments. We only want to run MergeSort once and then use that one result to resolve all queries.
'''


def MergeSortSelect(arr, query_list):
    # Only call MergeSort once
    # ... MergeSort has already been implemented for you (see below)
    pass
    return [(0, -1)] * len(query_list)  # replace this line with your return


##################################
#                                #
# Experiments: Mostly Complete   #
#                                #
##################################


def experiments():
    # Edit this parameter
    k = [1, 1, 1, 1, 1]

    # Feel free to edit these initial parameters

    RUNS = 20  # Number of runs for each trial; more runs means better distributions approximation but longer experiment
    HEIGHT = 1.5  # Height of a chart
    WIDTH = 3   # Width of a chart
    # Determines if subcharts share the same axis scale/limits
    # ... since the trails cover a wide range, sharing the same scale/limits can cause some lines to be too small.
    SAME_AXIS_SCALE = False

    # You do not need to edit anything below this line
    # ... however, you are free to investigate how it works

    # The search space for our parameters
    # DO NOT EDIT these parameters for your final figure
    n = [2 ** i for i in range(10, 16)]
    # Our deterministically generated dataset
    fixed_dataset = sorted([(0, K) for K in range(max(n))], key=lambda T: T[1], reverse=True)

    # Records we will use to create the Pandas DataFrame
    n_record = []
    k_record = []
    algorithm_record = []
    ms_record = []
    iter = 0
    for ni in n:
        dataset_size_n = fixed_dataset[:ni]
        for ki in k:
            # Generate the queries according to the problem set instructions specification
            queries = [round(j * ni / ki) for j in range(ki)]

            # QuickSelect Runs
            for _ in range(RUNS):
                # Record Time Taken to Solve All Queries
                start_time = time.time()
                for q in queries:
                    # Copy dataset just to be safe
                    QuickSelect(dataset_size_n.copy(), q)
                seconds = time.time() - start_time
                # Record this trial run
                n_record.append(ni)
                k_record.append(ki)
                ms_record.append(seconds * 1000)  # Convert seconds to milliseconds
                algorithm_record.append("QuickSelect")

            # MergeSort Runs
            for _ in range(RUNS):
                # Record Time Taken to Solve All Queries
                start_time = time.time()
                # Copy dataset just to be safe
                MergeSortSelect(dataset_size_n.copy(), queries)
                seconds = time.time() - start_time
                # Record this trial run
                n_record.append(ni)
                k_record.append(ki)
                ms_record.append(seconds * 1000)  # Convert seconds to milliseconds
                algorithm_record.append("MergeSort")

            # Print progress
            iter += 1
            print("{} of {} Trials Completed".format(iter, len(n) * len(k)))

    # Create Pandas DataFrame
    data_field_title = "Runtime for {} Runs (ms)".format(RUNS)
    df = pd.DataFrame({
        "N": n_record,
        "K": k_record,
        data_field_title: ms_record,
        "Algorithm": algorithm_record
    })
    plot(df, HEIGHT, WIDTH, SAME_AXIS_SCALE, data_field_title)


def plot(df, height, width, SAME_AXIS_SCALE, data_field_title):
    # Plot with Seaborn
    # ... Establish Rows by N
    # ... Establish Columns by K
    # ... Establish Lines by Algorithm
    g = sns.FacetGrid(df, row="N", col="K", hue="Algorithm", height=height, aspect=width / height,
                      sharex=SAME_AXIS_SCALE, sharey=SAME_AXIS_SCALE)
    # Plot the runtime value
    g.map(sns.kdeplot, data_field_title)
    g.add_legend()
    plt.show()


####################
#                  #
# Helper Functions #
#                  #
####################

def run():
    experiments()


# Feel free to use these function or code your own (as long as it is random)

# A small helper function to return a random integer
def get_random_int(start_inclusive, end_inclusive):
    # Uses the python random randomint function
    # ... this function takes in a start and end - both are inclusive [start,end]
    return random.randint(start_inclusive, end_inclusive)


# A small helper function to return a random integer
def get_random_index(arr):
    # retuns a number from 0 to len-1 for valid indices
    return get_random_int(0, len(arr) - 1)


#########################
#                       #
# Provided (Don't Edit) #
#                       #
#########################

#
# You Do NOT Need to Modify Anything Below This Line
#

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


'''
A deterministic sorting algorithm
arr: a list of Key-Value pair tuples
    e.g. [(K0, V0), (K1, V1), ..., (Ki, Vi), ..., (Kn, Vn)] 
returns: a sorted list, sorted according to keys
'''


def MergeSort(arr):
    if len(arr) < 2:
        return arr

    midpt = int(math.ceil(len(arr) / 2))

    half1 = MergeSort(arr[0:midpt])
    half2 = MergeSort(arr[midpt:])

    return merge(half1, half2)


if __name__ == "__main__":
    run()
