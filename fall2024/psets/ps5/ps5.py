from itertools import product, combinations

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
    Introduction: We've implemented exhaustive search, and the Bron Kerbosch algorithm for you below.

    You don't need to implement any extra code for this part.
'''

# Given an instance of the Graph class G, exhaustively search for a k-coloring
# Returns the coloring list if one exists, None otherwise.
def exhaustive_search_coloring(G, k=3):

    # Iterate through every possible coloring of nodes
    for coloring in product(range(0,k), repeat=G.N):
        G.colors = list(coloring)
        if G.is_graph_coloring_valid():
            return G.colors

    # If no valid coloring found, reset colors and return None
    G.reset_colors()
    return None

'''
IMPORTANT: get_maximal_isets(G) returns a *generator* of the maximal independent sets, not a list
           This means that instead of calculating all maximal isets at once, it spits them out one
           by one. One thing you could do is just turn that into a regular list, ie:

               isets = list(get_maximal_isets(G))

           And this will let the helper function generate all isets and toss them into a list.
           However, that might be inefficient in special cases where the first iset is enough to
           give you a solution (can you think of a graph where this is the case?). Therefore, it
           might be better to consider something like the following:

               for iset in get_maximal_isets(G):
                   do_something_with_iset(iset)

           Keep this in mind if you see that your code is timing out on the test cases - it might
           mean you need to use this helper function more intelligently.
'''

# Given an instance of the Graph class G, returns a generator of all maximal independent sets in G
# Uses helper function impelementing Bron-Kerbosch algorithm
def get_maximal_isets(G):
    yield from bron_kerbosch_max_indep_set(G, set(), set(range(G.N)), set())

#Bron-Kerbosch algorithm for finding all maximal independent sets in a graph
def bron_kerbosch_max_indep_set(G, R, P, X):
    if len(P)==0 and len(X)==0:
        yield R.copy()
    
    for vertex in P.copy():
        neighbors = set(G.edges[vertex]).union({vertex})
        new_P = P.intersection(set(range(G.N)).difference(neighbors))
        new_X = X.intersection(set(range(G.N)).difference(neighbors))
        yield from bron_kerbosch_max_indep_set(G, R.union({vertex}), new_P, new_X)
        
        P.remove(vertex)
        X.add(vertex)


'''
    Part A: Implement two coloring via breadth-first search.

    Hint: You will need to adapt the given BFS pseudocode so that it works on all graphs,
    regardless of whether they are connected.

    When you're finished, check your work by running python3 -m ps5_color_tests 2.
'''

# Given an instance of the Graph class G and a subset of precolored nodes,
# Assigns precolored nodes to have color 2, and attempts to color the rest using colors 0 and 1.
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
    
    # TODO: Complete this function by implementing two-coloring using the colors 0 and 1.
    # If there is no valid coloring, reset all the colors to None using G.reset_colors()
    
    G.reset_colors()
    return None



'''
    Part B: Implement the 3-coloring algorithm using the Bron-Kerbosch algorithm and BFS.
    
    Make sure to call the bfs_2_coloring function you implemented!

    When you're finished, check your work by running python3 -m ps5_color_tests 3.
    Don't worry if some of your tests time out: that is expected.
'''

# Given an instance of the Graph class G (which has a subset of precolored nodes), searches for a 3 coloring
# If successful, modifies G.colors and returns the coloring.
# If no coloring is possible, resets all of G's colors to None and returns None.
def iset_bfs_3_coloring(G):
    # TODO: Complete this function.

    G.reset_colors()
    return None

# Feel free to add miscellaneous tests below!
if __name__ == "__main__":
    G0 = Graph(2).add_edge(0, 1)
    print(bfs_2_coloring(G0))
    print(iset_bfs_3_coloring(G0))
