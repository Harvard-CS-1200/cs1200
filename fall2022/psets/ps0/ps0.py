#################
#               #
# Problem Set 0 #
#               #
#################

# Collaboration statement
#   worked with Sofia Lysenko and Anne Foley on this pset.
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
    # Top down approach 
    if not v:
        # if v is not a node that exists, return 0
        return 0
    elif (v.left == None) & (v.right == None):
        # if v is a leaf, return 1 and set its size to 1
        v.size = 1;
        return 1;
    else:
        # in all other cases, sum the sizes of v's children to get the size of v
        v.size = 1 + calculate_sizes(v.left) + calculate_sizes(v.right)
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
    # print(r.size)
    target = int((r.size)/2)
    # print(target)
    if (r == None) | (r.size == target) | ((r.left == None) & (r.right == None)):
        return r


    # only traverse to children 
    # index vertex
    c = r
    while(True):
        # Chris Barber showed me how to do one-line definitions
        left_size = c.left.size if c.left else 0
        right_size = c.right.size if c.right else 0

        if (left_size <= target) and (right_size <= target):
                ans = c
                break

        if left_size > right_size:
            c = c.left
        elif left_size < right_size:
            c = c.right
   
    return ans

    
