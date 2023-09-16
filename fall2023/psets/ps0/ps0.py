#################
#               #
# Problem Set 0 #
#               #
#################

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
    v.size = 1
    if v.left != None:
        v.size += calculate_sizes(v.left)
    if v.right != None:
        v.size += calculate_sizes(v.right)
    return v.size

#
# Problem 1c
#

# Input: BTvertex r, the root of a size-augmented BinaryTree T
# ... of size n and height h
# Output: A BTvertex that, if removed from the tree, would result
# ... in disjoint trees that all have at most n/2 vertices
# Runtime: O(h)
def findphiv(cur_node, n):
    l_sub = 0
    r_sub = 0
    parent_sub = n - cur_node.size
    if cur_node.left != None:
        l_sub = cur_node.left.size
    if cur_node.right != None:
        r_sub = cur_node.right.size
    return calc_potential(l_sub, r_sub, parent_sub, n, cur_node)

def calc_potential(lsize,rsize,psize, n, cur_node):
    largest_child = max(lsize,rsize)
    if max(lsize, rsize, psize) <= n/2:
         return cur_node
    elif largest_child == lsize and cur_node.left != None:
        return findphiv(cur_node.left, n)
    elif largest_child == rsize and cur_node.right != None:
        return findphiv(cur_node.right, n)
 
def find_vertex(r):
    tree_size = r.size
    return findphiv(r, tree_size)
