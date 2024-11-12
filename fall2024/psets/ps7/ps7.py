from itertools import product, combinations
from pysat.solvers import Glucose3

'''
Before you start: Read the README and the Graph implementation below.
'''

class Graph:
    '''
    A graph data structure with number of nodes N, list of sets of edges, and a list of color labels.
    Nodes and colors are both 0-indexed.
    For a given node u, its edges are located at self.edges[u] and its color is self.color[u].
    '''

    # Initializes the number of nodes, sets of edges for each node, and colors
    def __init__(self, N, edges = None, colors = None):
        self.N = N
        self.edges = [set(lst) for lst in edges] if edges is not None else [set() for _ in range(N)]
        self.colors = [c for c in colors] if colors is not None else [None for _ in range(N)]
    
    # Adds a node to the end of the list
    # Returns resulting graph
    def add_node(self):
        self.N += 1
        self.edges.append(set())
        return self
    
    # Adds an undirected edge from u to v
    # Returns resulting graph
    def add_edge(self, u, v):
        assert(v not in self.edges[u])
        assert(u not in self.edges[v])
        self.edges[u].add(v)
        self.edges[v].add(u)
        return self

    # Removes the undirected edge from u to v
    # Returns resulting graph
    def remove_edge(self, u, v):
        assert(v in self.edges[u])
        assert(u in self.edges[v])
        self.edges[u].remove(v)
        self.edges[v].remove(u)
        return self

    # Resets all colors to None
    # Returns resulting graph
    def reset_colors(self):
        self.colors = [None for _ in range(self.N)]
        return self

    def clone(self):
        return Graph(self.N, self.edges, self.colors)

    def clone_and_merge(self, g2, g1u, g2v):
        '''
        DOES NOT COPY COLORS
        '''
        g1 = self
        edges = g1.edges + [[v + g1.N for v in u_list] for u_list in g2.edges]
        g = Graph(g1.N + g2.N, edges)
        if g1u is not None and g2v is not None:
            g = g.add_edge(g1u, g2v + g1.N)
        return g

    # Checks if a given subset of nodes is an independent set 
    def is_independent_set(self, subset):
        for v in subset:
            for u in self.edges[v]:
                if u in subset:
                    return False
        return True

    # Checks all colors
    def is_graph_coloring_valid(self):
        for u in range(self.N):
            for v in self.edges[u]:

                # Check if every one has a coloring
                if self.colors[u] is None or self.colors[v] is None:
                    return False

                # Make sure colors on each edge are different
                if self.colors[u] == self.colors[v]:
                    return False
        
        return True

'''
    Introduction: We've implemented exhaustive search for you below.
    You don't need to implement any extra code for this part.
'''

# Given an instance of the Graph class G, exhaustively search for a k-coloring
# Returns the coloring list if one exists, None otherwise.
def exhaustive_search_coloring(G, k=3):

    # Iterate through every possible coloring of nodes
    for coloring in product(range(1,k+1), repeat=G.N):
        G.colors = list(coloring)
        if G.is_graph_coloring_valid():
            return G.colors

    # If no valid coloring found, reset colors and return None
    G.reset_colors()
    return None



'''
    We've implemented bfs_2_coloring for you below.
    You don't need to implement any extra code for this part.
'''

# Given an instance of the Graph class G and a subset of precolored nodes,
# Assigns precolored nodes to have color 2, and attempts to color the rest using colors 0 and 1.
#
# Precondition: Assumes that the precolored_nodes form an independent set.
# If successful, modifies G.colors and returns the coloring.
# If no coloring is possible, resets all of G's colors to None and returns None.
def bfs_2_coloring(G, precolored_nodes=None):
    # Assign every precolored node to have color 2
    # Initialize visited set to contain precolored nodes if they exist
    visited = set()
    G.reset_colors()
    preset_color = 2
    if precolored_nodes is not None:
        for node in precolored_nodes:
            G.colors[node] = preset_color
            visited.add(node)

        if len(precolored_nodes) == G.N:
            return G.colors

    # loop over source (for multiple connected components)
    for src in range(G.N):
        if src not in visited:
            # initialization
            frontier = [src]
            visited.add(src)
            G.colors[src] = 0
            # loop over frontiers
            while len(frontier) > 0:
                new_frontier = []

                for u in frontier:
                    for v in G.edges[u]:
                        # detect color conflict
                        if G.colors[u] == G.colors[v]:
                            G.reset_colors()
                            return None
                        # add v to new_frontier if not visited
                        if v not in visited:
                            new_frontier.append(v)
                            G.colors[v] = 1 - G.colors[u]
                            visited.add(v)
                frontier = new_frontier
    
    return G.colors

'''
    We've implemented iset_bfs_3_coloring for you below.
    You don't need to implement any extra code for this part.
'''
#Bron-Kerbosch algorithm for finding all maximal independent sets in a graph
def bron_kerbosch_max_indep_set(G, R, P, X):
    if len(P)==0 and len(X)==0:
        yield R.copy()

    if P.union(X):
        pivot_edges = G.edges[min(P.union(X), key=lambda v: len(G.edges[v]))]
    else:
        pivot_edges = set()

    for vertex in P.copy() - pivot_edges:
        neighbors = set(G.edges[vertex]).union({vertex})
        new_P = P.intersection(set(range(G.N)).difference(neighbors))
        new_X = X.intersection(set(range(G.N)).difference(neighbors))
        yield from bron_kerbosch_max_indep_set(G, R.union({vertex}), new_P, new_X)
        
        P.remove(vertex)
        X.add(vertex)

def max_indep_set_gen(G):
    yield from bron_kerbosch_max_indep_set(G, set(), set(range(G.N)), set())

# Given an instance of the Graph class G and a subset of precolored nodes, searches for a 3 coloring
def iset_bfs_3_coloring(G):
    for mis in max_indep_set_gen(G):
        coloring = bfs_2_coloring(G, precolored_nodes=mis)
        if coloring:
            return coloring
    return None

'''
    Part A: Implement the reduction to SAT. 
    Here, you should use the SAT solver that we've defined to add clauses, and use the built-in get_model function
    to find the solution if one exists.
    Link to documentation: https://pysathq.github.io/docs/html/api/solvers.html#pysat.solvers.Solver.get_model
    Hint: There are three parts to this problem.
    1. Transform the graph into an input that can be fed into the SAT solver.
    2. Run the solver using the solver.solve() and solver.get_model() functions. We have added this part for you.
    3. Transform the solver output into a valid coloring if one exists, else return None.
    When you're finished, check your work by running python3 -m ps8_color_tests 3.
    Don't worry if some of your tests time out: that is expected.
'''

# Given an instance of the Graph class G, reduces 3 coloring to SAT
# If successful, modifies G.colors and returns the coloring.
# If no coloring is possible, resets all of G's colors to None and returns None.
def sat_3_coloring(G):
    solver = Glucose3()

    # TODO: Add the clauses to the solver

    # Attempt to solve, return None if no solution possible
    if not solver.solve():
        G.reset_colors()
        return None

    # Accesses the model in form [-v1, v2, -v3 ...], which denotes v1 = False, v2 = True, v3 = False, etc.
    solution = solver.get_model()

    # TODO: If a solution is found, convert it into a coloring and update G.colors

    return G.colors

# Feel free to add miscellaneous tests below!
if __name__ == "__main__":
    G0 = Graph(2).add_edge(0, 1)
    print(bfs_2_coloring(G0))
    print(iset_bfs_3_coloring(G0))
    print(sat_3_coloring(G0))