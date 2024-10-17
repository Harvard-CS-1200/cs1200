import numpy as np
import signal

COLORS = ["BLUE", "GREEN", "RED", "YELLOW", "ORANGE", "PINK",
            "BLACK", "BROWN", "WHITE", "PURPLE"]

class timeout:
    def __init__(self, seconds=1, error_message='Timeout'):
        self.seconds = seconds
        self.error_message = error_message
    def handle_timeout(self, signum, frame):
        raise TimeoutError(self.error_message)
    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)
    def __exit__(self, type, value, traceback):
        signal.alarm(0)
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

def generate_random_graph(Graph, n, p):
    # generates complete graph but keeps edge with some probability
    assert(p >= 0 and p <= 1)
    g = Graph(n)
    for i in range(n):
        for j in range(n):
            if i < j and np.random.binomial(1, p) == 1:
                g.add_edge(i, j)
    return g

#  Checks all colors
def validate_graph_coloring(g, coloring):
    if coloring == None:
        return False
    self = g
    for u in range(g.N):
        for v in self.edges[u]:
            if coloring[u] is None or coloring[v] is None:
                return False
            if coloring[u] == coloring[v]:
                return False
    return True

def generate_complete_graph(Graph, n):
    g = Graph(n)
    for i in range(n):
        for j in range(n):
            if i < j:
                g.add_edge(i, j)
    return g

def generate_line_of_complete_subgraphs(Graph, number_of_subgraphs, size_of_complete_subgraph):
    assert(number_of_subgraphs > 0)
    g = generate_complete_graph(Graph, size_of_complete_subgraph)
    for _ in range(number_of_subgraphs - 1):
        g2 = generate_complete_graph(Graph, size_of_complete_subgraph)
        g = g2.clone_and_merge(g, size_of_complete_subgraph - 1, 0)
    return g

def generate_ring_graph(Graph, n):
    g = Graph(n)
    for i in range(n):
        u = i
        v = (i + 1) % n
        g.add_edge(u,v)
    return g

def generate_line_of_ring_subgraphs(Graph, number_of_subgraphs, size):
    assert(number_of_subgraphs > 0)
    g = generate_ring_graph(Graph, size)
    for _ in range(number_of_subgraphs - 1):
        g2 = generate_ring_graph(Graph, size)
        g = g2.clone_and_merge(g, size - 1, 0)
    return g

def generate_random_linked_cluster(Graph, cluster_size, number_of_clusters, p):
    n = cluster_size * number_of_clusters
    g = Graph(n)
    for u in range(n):
        for v in range(n):
            if u < v:
                if u // cluster_size != v // cluster_size:
                    if np.random.binomial(1, p) == 1:
                        g.add_edge(u, v)
    return g

def generate_line_of_complete_subgraphs(Graph, number_of_subgraphs, size_of_complete_subgraph):
    assert(number_of_subgraphs > 0)
    g = generate_complete_graph(Graph, size_of_complete_subgraph)
    for _ in range(number_of_subgraphs - 1):
        g2 = generate_complete_graph(Graph, size_of_complete_subgraph)
        g = g2.clone_and_merge(g, size_of_complete_subgraph - 1, 0)
    return g

#No longer used?
# Given an instance of the Graph class G and a subset of precolored nodes,
# Checks if subset is an independent set in G 
def is_independent_set(G, subset):
    for v in subset:
        for u in G.edges[v]:
            if u in subset:
                return False
    return True
