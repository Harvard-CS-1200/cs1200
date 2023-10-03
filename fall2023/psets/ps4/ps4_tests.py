from typing import OrderedDict
import random
from ps4 import QuickSelect, MergeSortSelect


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
    ORANGE = '\033[33m'


class Debugger:
    def __init__(self):
        self.counter = 0
        self._size_counter = 0

    def clear(self):
        self.counter = 0
        self._size_counter = 0

    def inc(self):
        self.counter += 1

    def count(self):
        return self.counter

    def inc_size_counter(self):
        self._size_counter += 1

    def size_counter(self):
        return self._size_counter


def multi_getattr(obj, attr, default=None):
    """
    Get a named attribute from an object; multi_getattr(x, 'a.b.c.d') is
    equivalent to x.a.b.c.d. When a default argument is given, it is
    returned when any attribute in the chain doesn't exist; without
    it, an exception is raised when a missing attribute is encountered.
    """
    attributes = attr.split(".")
    for i in attributes:
        try:
            obj = getattr(obj, i)
        except AttributeError:
            return default
    return obj


def generate_random_keyvalue(size, random_range):
    return [(random.randint(0, random_range - 1), 0) for _ in range(size)]


# def validate_QuickSelect(arr, target):
#     res = QuickSelect(arr, target)
#     sorted_list = sorted(arr, key=lambda T: T[1])
#     return res[1] == sorted_list[target][1]

def generate_test(name, size, random_range, target, hint_text=None):
    # print("finding random target", target)
    return {
        "label": name,
        "input": generate_random_keyvalue(size, random_range),
        "test": lambda arr: QuickSelect(arr, target)[0],
        "expected": lambda arr: sorted(arr, key=lambda T: T[0], reverse=False)[target][0],
        "show_expectation": True,
        "hint_text": hint_text
    }


def generate_keyvalue(keys):
    return [(K, 0) for K in keys]


def generate_mergesortselect_test(name, keys, targets, expected, hint_text=None):
    return {
        "label": name,
        "input": generate_keyvalue(keys),
        "test": lambda arr: [K for (K, _) in MergeSortSelect(arr, targets)],
        "expected": lambda arr: expected,
        "show_expectation": True,
        "hint_text": hint_text
    }


def test():
    tests = OrderedDict()

    hint = "This might fail if your implementation has a mistake in the inequlity conditions. Double check your implementation and the lecture notes."

    tests["QuickSelect Tests (only checks result not implementation):"] = [
        generate_test("Size 1 Array", 1, 10, 0),
        generate_test("Size 10 Array i = 0 small random range", 10, 5, 0),
        generate_test("Size 100 Array i = 0 small random range", 100, 5, 0),
        generate_test("Size 1000 Array i = 0 small random range", 1000, 5, 0),
        generate_test("Size 10 Array i = 9 small random range", 10, 5, 9),
        generate_test("Size 100 Array i = 99 small random range", 100, 5, 99),
        generate_test("Size 1000 Array i = 999 small random range", 1000, 5, 999),
        generate_test("Size 10 Array i = 0 large random range", 10, 100000, 0),
        generate_test("Size 100 Array i = 0 large random range", 100, 100000, 0),
        generate_test("Size 1000 Array i = 0 large random range", 1000, 100000, 0),
        generate_test("Size 10 Array i = 9 large random range", 10, 100000, 9),
        generate_test("Size 100 Array i = 99 large random range", 100, 100000, 99, hint),
        generate_test("Size 1000 Array i = 999 large random range", 1000, 100000, 999),
        generate_test("Size 10 Array random i", 10, 100000, random.randint(0, 9), hint),
        generate_test("Size 100 Array random i", 100, 100000, random.randint(0, 99), hint),
        generate_test("Size 1000 Array random i", 1000, 100000, random.randint(0, 999)),
    ]

    tests["MergeSortSelect Tests (only checks result not implementation):"] = [
        generate_mergesortselect_test("Size 1 Array with 1 Query", [8], [0], [8]),
        generate_mergesortselect_test("Size 5 Array with 1 Query", [8, 9, 10, 11, 12], [2], [10]),
        generate_mergesortselect_test("Size 5 Array with 3 Query", [8, 39, 104, 82, 12], [3], [82]),
        generate_mergesortselect_test("Size 5 Array with 3 Query", [8, 39, 104, 82, 12], [2], [39]),
        generate_mergesortselect_test("Size 5 Array with 5 Query", [1, 2, 3, 4, 5], [0, 1, 2, 3, 4], [1, 2, 3, 4, 5]),
        generate_mergesortselect_test("Size 5 Array Reversed with 5 Query", [5, 4, 3, 2, 1], [0, 1, 2, 3, 4],
                                      [1, 2, 3, 4, 5])
    ]

    number_passed = 0
    total_tests = 0
    for label, test_results in tests.items():
        print(label)

        for i, result in enumerate(test_results):
            # Print passed with test number and name
            # If failed, print failed and print the expected and received values
            res = result["test"](result["input"])
            expected = result["expected"](result["input"])
            con = res == expected
            number_passed += 1 if con else 0
            total_tests += 1
            col = color.GREEN if con else color.RED
            symbol = color.BOLD + col + (u'\u2713' if con else u'\u2717') + color.END + color.END
            print(symbol + " " + result["label"] + ": ", "Passed" if con else "Failed", end="")
            if (not con and ("show_expectation" not in result or result["show_expectation"])):
                print(" - Expected " + str(expected) + " But Got " + str(res), end="")
                if result["hint_text"]: print("\n\t" + color.ORANGE + u'\u26A0' + " " + result["hint_text"] + color.END,
                                              end="")
            print()

        print()
    col = color.GREEN if number_passed == total_tests else color.RED
    print(color.BOLD + "Tests Passed {}{}/{}".format(col, number_passed, total_tests) + color.END)


if __name__ == "__main__":
    test()