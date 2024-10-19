# Problem Set 5

## Overview

This problem set explores two algorithms for solving 3-coloring:
- Exhaustive search
- Augmentation of 2-coloring algorithm with Bron-Kerbosch

We have implemented exhaustive search for you as a benchmark. You will implement the BFS 2-coloring algorithm in part 3a and the ISET + BFS 3-coloring algorithm in parts 3b and 3c. In 1d, you will compare the performance of these algorithms.

*Make sure to pull from the course source often or check Ed for updates. We hope to release a perfect problem set but sometimes we add to the problem set to make things easier or fix obscure bugs.*

## Downloading Starter Code
Run the following command to download the necessary libraries for graphing:

```bash
pip install -r requirements.txt
```

## Instructions

**Problem 3a**: First, implement the O(n+m)-time algorithm for 2-coloring that we covered in class, verifying its correctness by running `python3 -m ps5_tests 2`.

**Problem 3b**: Implement the O(1.44^n)-time algorithm for 3-coloring using the Bron-Kerbosch algorithm and BFS, also verifying its correctness by running `python3 -m ps5_tests 3`.

To test the correctness of all of your coloring algorithms at once, you can run `python3 -m ps5_tests`.

**Problem 3c**: Run the experiments we provided in `ps5_experiments.py` and compare the efficiency of the two coloring algorithms in your writeup.

## Running the Code

The problem set includes some starter code in `ps5.py`. To run the code, type in your terminal:

```bash
python3 -m ps5
```

## Running the Included Tests

The problem set also includes some tests for you to test your code.

To run the tests, type in your terminal:

```bash
python3 -m ps5_tests 2
```

```bash
python3 -m ps5_tests 3
```

```bash
python3 -m ps5_experiments
```