import numpy as np
import signal
import random
from tqdm import tqdm
import networkx as nx
import pickle

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

def generate_hard_coloring_graphs_from_file(Graph, filename):
    with open(filename, 'r') as f:
        for line in f:
            if line[0] == 'c':
                continue
            if line[0] == 'p':
                n = int(line.split()[2])
                g = Graph(n)
                continue
            if line[0] == 'e':
                u, v = line.split()[1:]
                u = int(u) - 1
                v = int(v) - 1
                g.add_edge(u, v)
    return g

def get_edge_with_high_degree_node(g):
    while True:
            i = random.randint(0, g.N - 1)
            if len(g.edges[i]) <= 3 and len(g.edges[i]) > 0:
                j = random.choice(list(g.edges[i]))
                return i, j

def generate_hard_coloring_graphs(Graph, k):
    # 4 critical graphs to generate from as per the paper: https://www.sciencedirect.com/science/article/pii/S0166218X07001072#sec5
    critical_graphs = [
        # Graph(9).add_edge(0,1).add_edge(0,8).add_edge(1,2).add_edge(1,8).add_edge(1,5).add_edge(2,3)
        #         .add_edge(2,7).add_edge(3,4).add_edge(4,5).add_edge(5,6).add_edge(6,7).add_edge(7,8).add_edge(4,8),
        Graph(10).add_edge(0,1).add_edge(0,7).add_edge(0,8).add_edge(0,4).add_edge(1,7).add_edge(1,2).add_edge(1,5)
                   .add_edge(2,8).add_edge(2,9).add_edge(2,3).add_edge(3,4).add_edge(3,7).add_edge(4,9).add_edge(4,5)
                   .add_edge(5,6).add_edge(6,9).add_edge(6,8).add_edge(6,7),
        Graph(11).add_edge(0,1).add_edge(0,6).add_edge(0,9).add_edge(1,2).add_edge(1,7).add_edge(1,8).add_edge(2,8)
                   .add_edge(2,10).add_edge(2,3).add_edge(3,6).add_edge(3,4).add_edge(4,10).add_edge(4,5).add_edge(5,9)
                   .add_edge(5,6).add_edge(6,7).add_edge(7,8).add_edge(7,10).add_edge(8,9).add_edge(9,10),
        Graph(11).add_edge(0,1).add_edge(0,8).add_edge(0,4).add_edge(0,6).add_edge(1,2).add_edge(1,8).add_edge(2,10)
                   .add_edge(2,3).add_edge(3,10).add_edge(3,4).add_edge(3,5).add_edge(4,7).add_edge(5,7).add_edge(6,7)
                   .add_edge(7,9).add_edge(8,9).add_edge(9,10).add_edge(6,10).add_edge(5,8),
        Graph(12).add_edge(0,1).add_edge(1,2).add_edge(2,3).add_edge(3,4).add_edge(4,5).add_edge(5,6).add_edge(6,0)
                    .add_edge(7,8).add_edge(8,9).add_edge(9,10).add_edge(10,11).add_edge(11,7).add_edge(8,10).add_edge(7,5).add_edge(5,11)
                    .add_edge(0,7).add_edge(2,9).add_edge(6,10).add_edge(10,3).add_edge(11,1).add_edge(1,4).add_edge(4,8),
    ]

    # arbitrarily choose one of the critical graphs
    g = critical_graphs[2].clone()

    for _ in tqdm(range(k)):
        # Get a vertex with degree >= 3
        (i, j) = get_edge_with_high_degree_node(g)

        # Choose a random critical graph
        critical_graph = random.choice(critical_graphs).clone()
        # critical_graph = critical_graphs[2].clone()

        # Merge the critical graph with the current graph
        g = embed_graph(g, critical_graph, (i, j))

    return g


def embed_graph(g1, g2, e):
    i, j = e

    # Choose a random vertex in g2
    x, y = get_edge_with_high_degree_node(g2)
    
    g1.remove_edge(i, j)
    g2.remove_edge(x, y)

    g = g1.clone_and_merge(g2, j, y)

    # Merge x and i.
    # g.edges[x] = g.edges[x].union(g.edges[g2.N + i])
    # for e in g.edges[g2.N + i]:
    #     g.edges[e].remove(g2.N + i)
    #     g.edges[e].add(x)
    # g.edges[g2.N + i].clear()

    return g

def create_erdos_renyi_graph(n, cutoff=4.69):
    # Probability of edge creation
    # Suggestions: 
    # - 4.69 is the threshold between 3-colorable (<4.69) and non-3-colorable (>4.69) graphs
    # - To generate 3-colorable graphs with high probability, use a cutoff of <=4.60
    # - To generate non-3-colorable graphs with high probability, use a cutoff of >=4.80
    p = cutoff / n
    # Create Erdős-Rényi graph
    er_graph = nx.erdos_renyi_graph(n, p)
    return er_graph

def create_dense_core_graph(Graph, cycle_length):

    # Dense Core Graph
    core_vertices = 9
    num_cycles = int(core_vertices / 2)

    total_vertices = core_vertices + num_cycles * cycle_length
    graph = Graph(total_vertices)

    # generate and add cycles
    for i in range(core_vertices, total_vertices, cycle_length):
        # create cycle of length 6
        for j in range(cycle_length - 1):
            graph.add_edge(i + j, i + j + 1)
        # finish cycle - connect back to start
        graph.add_edge(i + cycle_length - 1, i)

        # connect cycle to two vertices, different for each cycle
        graph.add_edge(i, random.randint(0, core_vertices-1))
        graph.add_edge(i+1, random.randint(0, core_vertices-1))

    new_labels = list(range(0, total_vertices))
    random.shuffle(new_labels)

    # permute labels
    for i in range(total_vertices):
        temp = graph.edges[i]
        graph.edges[i] = graph.edges[new_labels[i]]
        graph.edges[new_labels[i]] = temp

    return graph

def convert_to_graph_object(Graph, G_nx):
    N = G_nx.number_of_nodes()
    edges = [set(neighbors) for _, neighbors in G_nx.adjacency()]
    return Graph(N, edges)