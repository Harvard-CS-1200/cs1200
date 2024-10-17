import numpy as np
import random
from ps5_helpers import timeout, color, generate_line_of_ring_subgraphs, generate_random_linked_cluster, COLORS
from ps5 import Graph, exhaustive_search_coloring, bfs_2_coloring, iset_bfs_3_coloring
random.seed(120)

##################################
#                                #
#          Experiments           #
#                                #
##################################

'''
    Part C: Run some tests to figure out the relative performance of the 3-coloring algorithms!
    We're comparing exhaustive search and ISET + BFS.

    There are two types of graphs we generate.
    1. Line of Rings:
        We generate rings and connect them together.
        Parameters to adjust:
            subgraph_line_parameter: number of rings in the line

    2. Randomized Cluster Connections (Semi Independent Sets):
        We create clusters of independent sets. Then, for each pair of nodes
        that are in different clusters, we add an edge between them with probability p.
        Parameters to adjust:
            cluster_graph_p_parameter: probability of joining an edge between two nodes in different clusters
            cluster_graph_cluster_size_parameter: number of nodes per cluster
            cluster_graph_cluster_quantity_parameter: number of clusters

    TIMEOUT_LENGTH: Number of seconds before an algorithm is set to time out.

    When you run the test file, you can see the performance of every combination of parameters
    and whether each algorithm timed out. Use the information from the printouts to answer question 1(d).
'''

# The timeout length in seconds
TIMEOUT_LENGTH = 1

def benchmark():
    # You may experiment with these parameters if you wish!
    # Each of these ranges is formatted with a minimum, maximum, and step size.
    subgraph_line_parameter_range = (100, 300, 100)
    cluster_graph_p_parameter_range = (0.2, 0.95, 0.15)
    cluster_graph_cluster_size_parameter_range = (2, 26, 8)
    cluster_graph_cluster_quantity_parameter_range = (2, 5, 1)

    algs = [("Exhaustive Coloring", lambda g: exhaustive_search_coloring(g)),
            ("ISET BFS Coloring", lambda g: iset_bfs_3_coloring(g))]

    print("Line of Rings")
    print()
    for r in [3,4,5]:
        print("Size of ring", r)
        for rings in range(subgraph_line_parameter_range[0], subgraph_line_parameter_range[1], subgraph_line_parameter_range[2]):
            print("\tNumber of rings", rings)
            g = generate_line_of_ring_subgraphs(Graph, rings, r)
            size_text = "\t(n = {}, m = {})".format(g.N, sum([len(v_lst) for v_lst in g.edges]) // 2)
            print(size_text)
            for (alg_name, alg) in algs:
                timedout = False
                try:
                    with timeout(seconds=TIMEOUT_LENGTH):
                        alg(g.clone())
                except TimeoutError:
                    timedout = True
                col = color.GREEN if not timedout else color.ORANGE
                if timedout:
                    symbol = color.BOLD + col + u'\u23f1' + color.END + color.END
                else:
                    symbol = color.BOLD + col + (u'\u2713' ) + color.END + color.END
                print("\t\t" + symbol + "  " + alg_name + ": ", ("Timeout" if timedout else "Finished"))

    print()
    print()
    print("Randomized Cluster Connections (Semi Independent Sets)")
    print()
    for p in np.arange(cluster_graph_p_parameter_range[0], cluster_graph_p_parameter_range[1], cluster_graph_p_parameter_range[2]):
        # print()
        print("Probability of keeping edge", p)
        for q in range(cluster_graph_cluster_quantity_parameter_range[0], cluster_graph_cluster_quantity_parameter_range[1], cluster_graph_cluster_quantity_parameter_range[2]):
            print("\tNumber of clusters", q)
            for s in range(cluster_graph_cluster_size_parameter_range[0], cluster_graph_cluster_size_parameter_range[1], cluster_graph_cluster_size_parameter_range[2]):
                # print()
                print("\t\tSize of cluster", s)
                g = generate_random_linked_cluster(Graph, s, q, p)
                size_text = "\t\t(n = {}, m = {})".format(g.N, sum([len(v_lst) for v_lst in g.edges]) // 2)
                print(size_text)
                for (alg_name, alg) in algs:
                    timedout = False
                    try:
                        with timeout(seconds=TIMEOUT_LENGTH):
                            alg(g.clone())
                    except TimeoutError:
                        timedout = True
                    col = color.GREEN if not timedout else color.ORANGE
                    if timedout:
                        symbol = color.BOLD + col + u'\u23f1' + color.END + color.END
                    else:
                        symbol = color.BOLD + col + (u'\u2713' ) + color.END + color.END
                    print("\t\t\t" + symbol + "  " + alg_name + ": ", ("Timeout" if timedout else "Finished"))

    
# random graph testing
if __name__ == "__main__":
    benchmark()
    
