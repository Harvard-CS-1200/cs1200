# Problem Set 4

## Overview

This problem set explores randomized algorithms and graphs. The programming portion of this problem set focuses on QuickSelect, a Las Vegas randomized algorithm.

*Make sure to pull from the course source often or check Ed for updates. We hope to release a perfect problem set but sometimes we add to the problem set to make things easier or fix obscure bugs.*

## Downloading Starter Code
Run the following command to download the necessary libraries for graphing:

```bash
pip install -r requirements.txt
```

## Instructions

**Problem 1a**: For this part of the problem, you must fill in the implementation for QuickSelect. We have provided some local tests to help you check that your implementation returns the right answer. You can run the included tests with `python3 -m ps4_tests` (as explained below). **If you pass the local tests you should be in good shape to move on. The focus of this problem is to implement a specific randomized algorithm.** It also sets up for the next parts of the problem.

**Problem 1b**: For this part, we have provided most of the code for plotting. You do not need to do much for this part of the problem except complete `MergeSortSelect`, experiment with different values for `k`, and possibly play around with the number of runs. `MergeSortSelect` should be an extension of `MergeSort` (provided) that runs `MergeSort` and resolves a number of queries, returning the results in one list/array. Once you have finished `MergeSortSelect`, you can test your implementation with the local tests (safe as for part 1a). After the local tests, you can start plotting. All the plotting logic and code is provided for you but feel free to adjust the plotting parameters. However, do not change `N` or the datasets for your final figure. Feel free to explore different number of `RUNS`. The more runs, the better we are able to approximate and plot the distribution; but more runs means it will take longer to complete, so set aside time to run these. It is set to 20, but if you have the time, experiment with different numbers of runs. To generate the chart run `python3 -m ps4` (as explained below). If you are having trouble fitting your generated chart on your screen, try changing the width and height parameters. **Make sure to save your generated chart and add it to your writeup.**

**Problem 1b (Continued)**: By this point in the class and in the problem set, you have implemented deterministic and randomized algorithms. We have also discussed runtime analysis but often times this hides constants that can make a difference in application; this is why we sometimes benchmark. Here you will analyze the benchmark to get a better understanding of the runtimes of randomized algorithms versus deterministic algorithms on a conceptual and practical level. Note that the conclusions we draw here are not for all randomized and deterministic algorithms, only our specific implementation of these two algorithms. In class, we went over a brief runtime analysis for QuickSelect. In reality, it might be wise to use MergeSort in some scenarios and QuickSelect in others. This is often true between two algorithms whether one be randomized and one deterministic or both are deterministic/randomized. This problem should make this idea concrete. **In this part of the problem, we want you to form your rationale on the data/figure from benchmarking and show how your intuition is developing in regard to using benchmarking to understand algorithm implementations.**


**Problem 1d (Optional)**: Add Median-of-3 QuickSelect to the experimental comparisons you performed above and interpret the results.

**Conclusion**: If your work passes the local tests, includes the figure for your generated chart, and answers 1b, you should be in good shape to get full marks for this problem.

## Running the Code

The problem set includes some starter code in `ps4.py`. To run the code, type in your terminal:

```bash
python3 -m ps4
```

## Running the Included Tests

The problem set also includes some tests for you to test your code.

To run the tests, type in your terminal:

```bash
python3 -m ps4_tests
```
