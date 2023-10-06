#################
#               #
# Problem Set 0 #
#               #
#################

# Alan Xu
# 2023-09-05


#
# Setup
#
class BinaryTree:
    def __init__(self, root):
        self.root: BTvertex = root
 
class BTvertex:
    def __init__(self, key):
        self.parent: BTvertex = None
        self.left: BTvertex = None
        self.right: BTvertex = None
        self.key: int = key
        self.size: int = None

#
# Problem 1a
#

# Input: BTvertex v, the root of a BinaryTree of size n
# Output: Up to you
# Side effect: sets the size of each vertex n in the
# ... tree rooted at vertex v to the size of that subtree
# Runtime: O(n)
def calculate_sizes(v):
    if not v:
        return 0
    v.size = calculate_sizes(v.left) + calculate_sizes(v.right) + 1
    return v.size

#
# Problem 1c
#

# Input: BTvertex r, the root of a size-augmented BinaryTree T
# ... of size n and height h
# Output: A BTvertex that, if removed from the tree, would result
# ... in disjoint trees that all have at most n/2 vertices
# Runtime: O(h)
def find_vertex(r): 
    if not r:
        return None
    target = r.size/2
    # set initial values
    current = r
    left = current.left.size if current.left else 0
    right = current.right.size if current.right else 0

    # run down the tree until the size of two child trees are below bound
    while (right > target or left > target):
        if right > left:
            current = current.right
        else:
            current = current.left
        left = current.left.size if current.left else 0
        right = current.right.size if current.right else 0
    return current
    
