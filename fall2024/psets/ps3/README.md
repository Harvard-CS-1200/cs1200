# Problem Set 3

## Overview

In this problem set, you will be building a RAM simulator in Python and using it to see the running times of different RAM programs.

## Writing the Simulator

Your first step will be implementing the different commands that your RAM simulator will support. In the `simulator.py` file, replace all the TODOs and `pass` statements with your own code.

## Running the Experiments

For Problem 2, we ask you to implement the two RAM programs. Fill out these programs under `prog1` and `prog2`, respectively. Once you have done this, you can use our provided graphing template to plot the running times of each program.

To generate and save the plots as a `running_times.png` file, run:

```bash
python3 experiments.py
```

You likely already have matplotlib installed due to the RadixSort graph problem on pset 1, but in case you don't you can install it with:

```bash
python3 -m pip install matplotlib
```

## Running the Included Tests

The problem set also includes some tests for you to test your code.

**Note:** Passing all included (local) tests does not necessarily mean your code is correct, or that you will get a 100%, but it is a good start. Do your best to check base cases, corner cases, and robustness on your own.

To run the tests, type in your terminal:

```bash
python3 tests.py
```

## Finished Early?

Write your own RAM program to test your simulator!
