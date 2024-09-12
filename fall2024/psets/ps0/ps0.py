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
        """
        :param root: the root of the binary tree
        """
        self.root: BTvertex = root
 
class BTvertex:
    def __init__(self, key):
        """
        :param: the key associated with the vertex of the binary tree
        """
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
    # Checking to make sure that v exists, if not then return none
    if v is None:
        return 0
    # Calculating size of v by adding vertices and 1 for the root
    v.size = 1 + calculate_sizes(v.left) + calculate_sizes(v.right)

    return v.size


#
# Problem 1c
#

# Input: a positive integer t, 
# ...BTvertex v, the root of a BinaryTree of size n >= 1
# Output: BTvertex, descendent of v such that its size is between 
# ... t and 2t (inclusive)
# Runtime: O(h) 

def FindDescendantOfSize(t, v):
    # Checking the size of v, if it falls within bounds, return v
    if v.size >= t and v.size <= 2*t:
        return v

    # Checking to make sure that v left exists and that it holds some value
    if v.left and v.size is not None:
        # return value of v left and t if it exists
        return FindDescendantOfSize(t, v.left)

    # Checking v right
    if v.right:
        # return the value of v right and t when checking its value
        return FindDescendantOfSize(t,v.right)