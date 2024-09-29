# Local tests for your simulator
# Run `python tests.py` to see the results

import simulator

from typing import OrderedDict

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

tests = OrderedDict()

# variables
input_len_id = 0
output_ptr_id = 1
output_len_id = 2
zero_id = 3
one_id = 4
counter_id = 5
result_id = 6
two_id = 7    # Used only in log

# RAM Program computing factorial
fac = [7, 
            ['assign', zero_id, 0],
            ['assign', one_id, 1],
            ['assign', output_len_id, 1], 
            ['assign', output_ptr_id, 0], 
            ['assign', result_id, 1],
            ['read', counter_id, zero_id],
            ['goto', counter_id, 10],
            ['*', result_id, result_id, counter_id],
            ['-', counter_id, counter_id, one_id],
            ['goto', zero_id, 6],
            ['write', output_ptr_id, result_id],
        ]

# RAM Program computing floor of log base 2
log = [8, 
            ['assign', zero_id, 0],
            ['assign', one_id, 1],
            ['assign', two_id, 2],
            ['assign', output_len_id, 1], 
            ['assign', output_ptr_id, 0], 
            ['assign', result_id, -1],
            ['read', counter_id, zero_id],
            ['goto', counter_id, 11],
            ['+', result_id, result_id, one_id],
            ['/', counter_id, counter_id, two_id],
            ['goto', zero_id, 7],
            ['write', output_ptr_id, result_id],
        ]

# Computes subtraction of two vars, returns 0 (clamped)
minus = [5, 
            ['assign', output_len_id, 1], 
            ['assign', output_ptr_id, 0], 
            ['assign', 3, 3],
            ['assign', 4, 15],
            ['-', 3, 3, 4],
            ['write', output_ptr_id, 3],
        ]

# Computes division of two vars, returns 0 (clamped)
divide = [5, 
            ['assign', output_len_id, 1], 
            ['assign', output_ptr_id, 0], 
            ['assign', 3, 3],
            ['assign', 4, 0],
            ['/', 3, 3, 4],
            ['write', output_ptr_id, 3],
        ]

def test() :
    tests["Example 0: Unit Tests"] = [
        {
            "label": "Subtract",
            "input": 0,
            "test": lambda n: simulator.executeProgram(minus, [0])[0],
            "expected": 0,
            "show_expectation": True
        },
        {
            "label": "Divide",
            "input": 0,
            "test": lambda n: simulator.executeProgram(divide, [0])[0],
            "expected": 0,
            "show_expectation": True
        },
        # TODO: Add more test cases
    ]
    tests["Example 1: Factorial Tests"] = [
        {
            "label": "Factorial(0)",
            "input": 0,
            "test": lambda n: simulator.executeProgram(fac, [n])[0],
            "expected": 1,
            "show_expectation": True
        },
        {
            "label": "Factorial(1)",
            "input": 1,
            "test": lambda n: simulator.executeProgram(fac, [n])[0],
            "expected": 1,
            "show_expectation": True
        },
        {
            "label": "Factorial(2)",
            "input": 2,
            "test": lambda n: simulator.executeProgram(fac, [n])[0],
            "expected": 2,
            "show_expectation": True
        },
        {
            "label": "Factorial(3)",
            "input": 3,
            "test": lambda n: simulator.executeProgram(fac, [n])[0],
            "expected": 6,
            "show_expectation": True
        },
        {
            "label": "Factorial(5)",
            "input": 5,
            "test": lambda n: simulator.executeProgram(fac, [n])[0],
            "expected": 120,
            "show_expectation": True
        },
        {
            "label": "Factorial(10)",
            "input": 10,
            "test": lambda n: simulator.executeProgram(fac, [n])[0],
            "expected": 3628800,
            "show_expectation": True
        },
    ]
    tests["Example 2: Log Tests"] = [
        {
            "label": "Log(1)",
            "input": 1,
            "test": lambda n: simulator.executeProgram(log, [n])[0],
            "expected": 0,
            "show_expectation": True
        },
        {
            "label": "Log(2)",
            "input": 2,
            "test": lambda n: simulator.executeProgram(log, [n])[0],
            "expected": 1,
            "show_expectation": True
        },
        {
            "label": "Log(3)",
            "input": 3,
            "test": lambda n: simulator.executeProgram(log, [n])[0],
            "expected": 1,
            "show_expectation": True
        },
        {
            "label": "Log(4)",
            "input": 4,
            "test": lambda n: simulator.executeProgram(log, [n])[0],
            "expected": 2,
            "show_expectation": True
        },
        {
            "label": "Log(16)",
            "input": 16,
            "test": lambda n: simulator.executeProgram(log, [n])[0],
            "expected": 4,
            "show_expectation": True
        },
        {
            "label": "Log(19)",
            "input": 19,
            "test": lambda n: simulator.executeProgram(log, [n])[0],
            "expected": 4,
            "show_expectation": True
        },
        {
            "label": "Log(32)",
            "input": 32,
            "test": lambda n: simulator.executeProgram(log, [n])[0],
            "expected": 5,
            "show_expectation": True
        },
        {
            "label": "Log(1024)",
            "input": 1024,
            "test": lambda n: simulator.executeProgram(log, [n])[0],
            "expected": 10,
            "show_expectation": True
        },
        ]     

    number_passed = 0
    total_tests = 0
    for label, test_results in tests.items():
        print(label)

        for i, result in enumerate(test_results):
            # Print passed with test number and name
            # If failed, print failed and pring the expected and recieved values
            res = result["test"](result["input"])
            con = res == result["expected"]
            number_passed += 1 if con else 0
            total_tests += 1
            col = color.GREEN if con else color.RED
            symbol = color.BOLD + col + (u'\u2713' if con else u'\u2717') + color.END + color.END
            print(symbol + " " + result["label"] + ": ", "Passed" if con else "Failed", end="")
            if (not con and ("show_expectation" not in result or result["show_expectation"])):
                print(" - Expected " +
                        str(result["expected"]) + " But Got " + str(res), end="")
            print()
        print()
    col = color.GREEN if number_passed == total_tests else color.RED
    print(color.BOLD + "Tests Passed {}{}/{}".format(col, number_passed, total_tests) + color.END)


if __name__ == "__main__":
    test()