#################
#               #
# Problem Set 0 #
#               #
#################


#
# Setup
#

class BTvertex:
    # parent: BTvertex (or None in the case of the root)
    # left : BTvertex
    # right : BTvertex
    # key : string
    # temp : int
    def __init__(self, key):
        self.parent = None
        self.left = None
        self.right = None
        self.key = key
        self.size = None

class BinaryTree:
    #root: BTvertex
    def __init__(self, root):
        self.root = root


#
# Problem 1a
#

# Input: BTvertex v, the root of a BinaryTree of size n
# Output: Up to you
# Side effect: sets the size of each vertex n in the
# ... tree rooted at vertex v to the size of that subtree
# Runtime: O(n)
def calculate_sizes(v):
    # Your code goes here
    pass

#
# Problem 1c
#

# Input: BTvertex r, the root of a size-augmented BinaryTree T
# ... of size n and height h
# Output: A BTvertex that, if removed from the tree, would result
# ... in disjoint trees that all have at most n/2 vertices
# Runtime: O(h)
def find_vertex(r):
    # Your code goes here
    pass
