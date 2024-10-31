# Problem Set 7

## Overview

In problem set 5, we explored two algorithms for solving 3-coloring. In this problem set we will cover an additional way to solving 3-coloring - reduction to SAT.

We already implemented exhaustive search and augmentation of 2-coloring algorithm with independent sets in problem set 5. You will implement the reduction to SAT in 1a. In 1b, you will compare the performance of these three algorithms.

*Make sure to pull from the course source often or check Ed for updates. We hope to release a perfect problem set but sometimes we add to the problem set to make things easier or fix obscure bugs.*

## Instructions

**Problem 1a**: Implement the reduction from 3-coloring to SAT given in class,  producing an input that can be fed into the SAT Solver Glucose, and verify its correctness by running `python3 -m ps7_tests`.

**Problem 1b**: Run the algorithm on the generated graphs via `ps7_experiments.py`.

## Running the Code

The problem set includes some starter code in `ps7.py`. To run the code, type in your terminal:

```bash
python3 -m ps7
```

## Running the Included Tests

The problem set also includes some tests for you to test your code.

To run the tests, type in your terminal:

```bash
python3 -m ps7_tests
```

```bash
python3 -m ps7_experiments
```
