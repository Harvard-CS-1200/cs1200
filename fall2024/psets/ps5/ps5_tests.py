from typing import OrderedDict
import random
random.seed(120)
from ps5_helpers import timeout, color, generate_line_of_ring_subgraphs, generate_random_linked_cluster, validate_graph_coloring, generate_line_of_complete_subgraphs, generate_complete_graph
from ps5 import Graph, exhaustive_search_coloring, bfs_2_coloring, iset_bfs_3_coloring


TIMEOUT_LENGTH = 1
INCLUDE_TESTS_FOR_STAFF_CODE = False

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

def generate_random_itemkey(size, random_range):
    return [(0, random.randint(0, random_range - 1)) for _ in range(size)]

def timeout_input(alg):
    with timeout(seconds=TIMEOUT_LENGTH):
        return alg()

def timeout_test(alg, arr):
    with timeout(seconds=TIMEOUT_LENGTH):
        return alg(arr)

def run_tests(tests):
    number_passed = 0
    total_tests = 0
    for label, test_results in tests.items():
        print(label)

        for i, result in enumerate(test_results):
            # Print passed with test number and name
            # If failed, print failed and pring the expected and recieved values
            timedout = False
            try:
                input = result["input"]()
                res = result["test"](input)
            except TimeoutError:
                timedout = True
            except RecursionError:
                timedout = True
            if timedout:
                col = color.RED
                total_tests += 1
                symbol = color.BOLD + col + u'\u231b' + color.END + color.END
                symbol = color.BOLD + col + u'\u23f1' + color.END + color.END
                print(symbol + "  " + result["label"] + ": ", "Timeout", end="")
            else:
                expected = result["expected"](input)
                con = res == expected
                number_passed += 1 if con else 0
                total_tests += 1
                col = color.GREEN if con else color.RED
                symbol = color.BOLD + col + (u'\u2713' if con else u'\u2717') + color.END + color.END
                print(symbol + " " + result["label"] + " (n = {}, m = {})".format(input.N, sum([len(v_lst) for v_lst in input.edges]) // 2) + ": ", "Passed" if con else "Failed", end="")
                if (not con and ("show_expectation" not in result or result["show_expectation"])):
                    print(" - Expected " + str(expected) + " But Got " + str(res), end="")
                    if result["hint_text"]: print("\n\t" + color.ORANGE + u'\u26A0' + " " + result["hint_text"] + color.END, end="")
            print("", flush=True)

        print()
    col = color.GREEN if number_passed == total_tests else color.RED
    if number_passed != total_tests:
        print("Consider checking the following:")
        print("\t Does your algorithm work with a small number of nodes (specifically < 3)")
        print("\t Do you validate the subset that you selected? (i.e. check that S is an independent set)")
        print("\t Check the note above the get_max_indep_sets method - have you used the Python generator correctly?")
        print("")
    print(color.BOLD + "Tests Passed {}{}/{}".format(col, number_passed, total_tests) + color.END)

def generate_test(name, input, alg, expected, hint_text = None):
    return {
        "label": name,
        "input": lambda: timeout_input(input),
        "test": lambda arr: timeout_test(alg, arr),
        "expected": lambda g: expected(g),
        "show_expectation": True,
        "hint_text": hint_text
    }

testcases = {
    "2-colorable": [
        lambda: Graph(2).add_edge(0, 1), # line length 2
        lambda: Graph(2).add_edge(1, 0), # line length 2
        lambda: Graph(4).add_edge(0, 1).add_edge(1, 2).add_edge(2, 3), # line length 4
        lambda: Graph(4).add_edge(0, 1).add_edge(1, 2).add_edge(2, 3).add_edge(3, 0), # sqaure
        lambda: Graph(8).add_edge(0, 1).add_edge(1, 2).add_edge(2, 3).add_edge(3, 0).add_edge(0, 4).add_edge(1, 5).add_edge(2, 6).add_edge(3,7), # sqaure with line out of each node
        lambda: Graph(8).add_edge(0, 1).add_edge(1, 2).add_edge(2, 3).add_edge(3, 4).add_edge(4, 5).add_edge(5, 6).add_edge(7, 0).clone_and_merge(Graph(8).add_edge(0, 1).add_edge(1, 2).add_edge(2, 3).add_edge(3, 4).add_edge(4, 5).add_edge(5, 6).add_edge(7, 0), None, None), # sqaure with line out of each node
        lambda: Graph(8).add_edge(0, 1).add_edge(1, 2).add_edge(2, 3).add_edge(3, 4).add_edge(4, 5).add_edge(5, 6).add_edge(7, 0).clone_and_merge(Graph(8).add_edge(0, 1).add_edge(1, 2).add_edge(2, 3).add_edge(3, 4).add_edge(4, 5).add_edge(5, 6).add_edge(7, 0), 0, 0), # sqaure with line out of each node
    ],
    "2-colorable-large": [
        lambda: generate_random_linked_cluster(Graph, 200, 2, 0.3),
        lambda: generate_random_linked_cluster(Graph, 200, 2, 0.5),
        lambda: generate_random_linked_cluster(Graph, 200, 2, 0.7),
        lambda: generate_line_of_complete_subgraphs(Graph, 200, 2),
        lambda: generate_line_of_complete_subgraphs(Graph, 400, 2),
        lambda: generate_line_of_complete_subgraphs(Graph, 600, 2),
    ],
    "2-or-3-colorable": [
        lambda: generate_line_of_ring_subgraphs(Graph, 10, 4),
        lambda: generate_random_linked_cluster(Graph, 100, 2, 0.3),
        lambda: generate_random_linked_cluster(Graph, 100, 2, 0.5),
        lambda: generate_random_linked_cluster(Graph, 100, 2, 0.7),
    ],
    "2-or-3-colorable-large": [
        lambda: generate_random_linked_cluster(Graph, 200, 2, 0.3),
        lambda: generate_random_linked_cluster(Graph, 200, 2, 0.5),
        lambda: generate_random_linked_cluster(Graph, 200, 2, 0.7),
    ],
    "3-colorable": [
        lambda: Graph(3).add_edge(0, 1).add_edge(1, 2).add_edge(2, 0), # 3 node triangle
        lambda: Graph(3).add_edge(1, 2).add_edge(2, 0).add_edge(0, 1), # 3 node triangle
        lambda: Graph(3).add_edge(2, 0).add_edge(0, 1).add_edge(1, 2), # 3 node triangle
        lambda: Graph(6).add_edge(2, 0).add_edge(0, 1).add_edge(1, 2).add_edge(3, 4).add_edge(4, 5).add_edge(5, 3), # 3 node triangle x2 disconnected
        lambda: Graph(6).add_edge(0, 1).add_edge(1, 2).add_edge(2, 0).add_edge(3, 4).add_edge(4, 5).add_edge(5, 3), # 3 node triangle x2 disconnected
        lambda: Graph(6).add_edge(1, 2).add_edge(2, 0).add_edge(0, 1).add_edge(3, 4).add_edge(4, 5).add_edge(5, 3), # 3 node triangle x2 disconnected
        lambda: Graph(6).add_edge(1, 2).add_edge(2, 0).add_edge(0, 1).add_edge(0, 3).add_edge(1, 4).add_edge(1, 5), # 3 node triangle with line out of each node
        # 3 node triangle with 2 line out of each node
        lambda: Graph(9).add_edge(1, 2).add_edge(2, 0).add_edge(0, 1).add_edge(0, 3).add_edge(1, 4).add_edge(1, 5).add_edge(0, 6).add_edge(1, 7).add_edge(1, 8), 
        # 3 node triangle with 2 line out of each node
        lambda: Graph(9).add_edge(2, 0).add_edge(0, 1).add_edge(1, 2).add_edge(0, 3).add_edge(1, 4).add_edge(1, 5).add_edge(0, 6).add_edge(1, 7).add_edge(1, 8),
        lambda: generate_complete_graph(Graph, 3).clone_and_merge(generate_complete_graph(Graph, 3), 2, 0).clone_and_merge(generate_complete_graph(Graph, 3), 5, 0).clone_and_merge(generate_complete_graph(Graph, 3), 8, 0),
        lambda: generate_line_of_complete_subgraphs(Graph, 2, 3),
        lambda: generate_line_of_complete_subgraphs(Graph, 3, 3),
        lambda: generate_line_of_complete_subgraphs(Graph, 4, 3),
        lambda: generate_line_of_complete_subgraphs(Graph, 5, 3),
        lambda: generate_line_of_complete_subgraphs(Graph, 6, 3),
    ],
    "3-colorable-large": [
        lambda: generate_line_of_ring_subgraphs(Graph, 10, 3),
        lambda: generate_line_of_ring_subgraphs(Graph, 10, 5),
        lambda: generate_line_of_complete_subgraphs(Graph, 20, 3),
        lambda: generate_line_of_complete_subgraphs(Graph, 40, 3),
        lambda: generate_line_of_complete_subgraphs(Graph, 60, 3),
        lambda: generate_line_of_complete_subgraphs(Graph, 80, 3),
        lambda: generate_line_of_complete_subgraphs(Graph, 100, 3),
        lambda: generate_line_of_complete_subgraphs(Graph, 150, 3),
        lambda: generate_line_of_complete_subgraphs(Graph, 200, 3),
        lambda: generate_line_of_complete_subgraphs(Graph, 400, 3),
        lambda: generate_line_of_complete_subgraphs(Graph, 600, 3),
        lambda: generate_line_of_complete_subgraphs(Graph, 800, 3),
        lambda: generate_line_of_complete_subgraphs(Graph, 1000, 3),
        lambda: generate_line_of_complete_subgraphs(Graph, 7, 3),
        lambda: generate_line_of_complete_subgraphs(Graph, 8, 3),
        lambda: generate_line_of_complete_subgraphs(Graph, 9, 3),
        lambda: generate_line_of_complete_subgraphs(Graph, 10, 3),
        lambda: generate_line_of_complete_subgraphs(Graph, 11, 3),
        lambda: generate_line_of_complete_subgraphs(Graph, 12, 3),
        lambda: generate_line_of_complete_subgraphs(Graph, 15, 3),
    ],
    "k>3-colorable": [
        lambda: generate_complete_graph(Graph, 4),
        lambda: generate_complete_graph(Graph, 5),
        lambda: generate_complete_graph(Graph, 6),
        lambda: generate_complete_graph(Graph, 3).clone_and_merge(generate_complete_graph(Graph, 4), None, None),
        lambda: generate_complete_graph(Graph, 4).clone_and_merge(generate_complete_graph(Graph, 3), None, None),
        lambda: generate_complete_graph(Graph, 7).clone_and_merge(generate_complete_graph(Graph, 3), None, None),
        lambda: generate_complete_graph(Graph, 2).clone_and_merge(generate_complete_graph(Graph, 4), None, None),
        lambda: generate_complete_graph(Graph, 4).clone_and_merge(generate_complete_graph(Graph, 2), None, None),
        lambda: generate_complete_graph(Graph, 7).clone_and_merge(generate_complete_graph(Graph, 2), None, None),
        lambda: generate_complete_graph(Graph, 7),
    ],
    "k>3-colorable-large": [
        lambda: generate_line_of_complete_subgraphs(Graph, 20, 4),
        lambda: generate_line_of_complete_subgraphs(Graph, 20, 5), 
    ]
}


def test_2_coloring():
    tests = OrderedDict()

    if INCLUDE_TESTS_FOR_STAFF_CODE:
        tests["Exhaustive 2-Coloring (Staff Provided)"] = [] 
        tests["Exhaustive 2-Coloring (Staff Provided)"] += [generate_test("Should work on 2-colorable graphs", g, lambda g: validate_graph_coloring(g, exhaustive_search_coloring(g, 2)), lambda g: True) for g in testcases["2-colorable"]]


    tests["BFS 2-Coloring (Staff Provided)"] = [] 
    tests["BFS 2-Coloring (Staff Provided)"] += [generate_test("Should work on 2-colorable graphs", g, lambda g: validate_graph_coloring(g, bfs_2_coloring(g)), lambda g: True) for g in testcases["2-colorable"]]

    run_tests(tests)

def test_3_coloring():
    tests = OrderedDict()

    if INCLUDE_TESTS_FOR_STAFF_CODE:
        tests["Exhaustive 3-Coloring (Staff Provided)"] = [] 
        tests["Exhaustive 3-Coloring (Staff Provided)"] += [generate_test("Should work on 2-colorable graphs", g, lambda g: validate_graph_coloring(g, exhaustive_search_coloring(g, 3)), lambda g: True) for g in testcases["2-colorable"]]
        tests["Exhaustive 3-Coloring (Staff Provided)"] += [generate_test("Should work on 2-or-3-colorable graphs", g, lambda g: validate_graph_coloring(g, exhaustive_search_coloring(g, 3)), lambda g: True) for g in testcases["2-or-3-colorable"]]
        tests["Exhaustive 3-Coloring (Staff Provided)"] += [generate_test("Should work on 3-colorable graphs", g, lambda g: validate_graph_coloring(g, exhaustive_search_coloring(g, 3)), lambda g: True) for g in testcases["3-colorable"]]
        tests["Exhaustive 3-Coloring (Staff Provided)"] += [generate_test("Should not work on k>3-colorable graphs", g, lambda g: validate_graph_coloring(g, exhaustive_search_coloring(g, 3)), lambda g: False) for g in testcases["k>3-colorable"]]

    tests["ISET 3-Coloring (Staff Provided)"] = [] 
    tests["ISET 3-Coloring (Staff Provided)"] += [generate_test("Should work on 2-colorable graphs", g, lambda g: validate_graph_coloring(g, iset_bfs_3_coloring(g)), lambda g: True) for g in testcases["2-colorable"]]
    tests["ISET 3-Coloring (Staff Provided)"] += [generate_test("Should work on large 2-colorable graphs", g, lambda g: validate_graph_coloring(g, iset_bfs_3_coloring(g)), lambda g: True) for g in testcases["2-colorable-large"]]
    tests["ISET 3-Coloring (Staff Provided)"] += [generate_test("Should work on 2-or-3-colorable graphs", g, lambda g: validate_graph_coloring(g, iset_bfs_3_coloring(g)), lambda g: True) for g in testcases["2-or-3-colorable"]]
    tests["ISET 3-Coloring (Staff Provided)"] += [generate_test("Should work on 3-colorable graphs", g, lambda g: validate_graph_coloring(g, iset_bfs_3_coloring(g)), lambda g: True) for g in testcases["3-colorable"]]
    tests["ISET 3-Coloring (Staff Provided)"] += [generate_test("Should not work on k>3-colorable graphs", g, lambda g: validate_graph_coloring(g, iset_bfs_3_coloring(g)), lambda g: False) for g in testcases["k>3-colorable"]]

    run_tests(tests)


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        test_2_coloring()
        test_3_coloring()
    else:
        if sys.argv[1] == '2':
            test_2_coloring()
        elif sys.argv[1] == '3':
            test_3_coloring()
        else:
            print("Please pass in a valid argument (2 or 3)")

