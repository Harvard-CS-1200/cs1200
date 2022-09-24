class BinarySearchTree:
    # left: BinarySearchTree
    # right: BinarySearchTree
    # key: int
    # item: int
    # size: int
    def __init__(self, debugger = None):
        self.left = None
        self.right = None
        self.key = None
        self.item = None
        self._size = 1
        self.debugger = debugger

        # add parent attribute?? 

    @property
    def size(self):
         return self._size
       
     # a setter function
    @size.setter
    def size(self, a):
        debugger = self.debugger
        if debugger:
            debugger.inc_size_counter()
        self._size = a

    ####### Part a #######
    '''
    Calculates the size of the tree
    returns the size at a given node
    '''
    def calculate_sizes(self, debugger = None):
        # Debugging code
        # No need to modify
        # Provides counts
        if debugger is None:
            debugger = self.debugger
        if debugger:
            debugger.inc()

        # Implementation
        self.size = 1
        if self.right is not None:
            self.size += self.right.calculate_sizes(debugger)
        if self.left is not None:
            self.size += self.left.calculate_sizes(debugger)
        return self.size

    '''
    Select the ind-th key in the tree
    
    ind: a number between 0 and n-1 (the number of nodes/objects)
    returns BinarySearchTree/Node or None
    '''
    def select(self, ind):
        left_size = 0
        if self.left is not None:
            left_size = self.left.size
        if ind == left_size:
            return self
        if left_size > ind and self.left is not None:
            return self.left.select(ind)
        elif left_size < ind and self.right is not None:
            return self.right.select(ind-left_size-1)
        return None


    '''
    Searches for a given key
    returns a pointer to the object with target key or None (Roughgarden)
    '''
    def search(self, key):
        if self is None:
            return None
        elif self.key == key:
            return self
        elif self.key < key and self.right is not None:
            return self.right.search(key)
        elif self.left is not None:
            return self.left.search(key)
        return None
    

    '''
    Inserts a key into the tree
    key: the key for the new node; 
        ... this is NOT a BinarySearchTree/Node, the function creates one
    
    returns the original (top level) tree - allows for easy chaining in tests
    '''
    def insert(self, key):
        if self.key is None:
            self.key = key
        # should be greater than or equal to, next elif should be an else
        elif self.key > key: 
            if self.left is None:
                self.left = BinarySearchTree(self.debugger)
                self.left.size = 1
            self.size +=1
            self.left.insert(key)
        elif self.key < key:
            if self.right is None:
                self.right = BinarySearchTree(self.debugger)
                self.right.size = 1
            self.size +=1
            self.right.insert(key)

        # self.calculate_sizes()

        # change: commented out self.calculate_sizes() and replaced with
        # lines that simply increment the size of nodes on path to new
        # node by 1

        return self

    
    ####### Part b #######

    '''
    Performs a `direction`-rotate the `side`-child of (the root of) T (self)
    direction: "L" or "R" to indicate the rotation direction
    child_side: "L" or "R" which child of T to perform the rotate on
    Returns: the root of the tree/subtree
    Example:
    Original Graph
      10
       \
        11
          \
           12
    
    Execute: NodeFor10.rotate("L", "R") -> Outputs: NodeFor10
    Output Graph
      10
        \
        12
        /
       11 
    '''
    def rotate(self, direction, child_side):
        # Your code goes here
        if child_side == "R" and self.right:
            if direction == "R":
                # self.calculate_sizes()
                old_r = self.right #x size y + c +1
                new_r = self.right.left # y size a+b+1
                old_r.left = new_r.right
                old_r.size = (old_r.left.size if old_r.left else 0) + (old_r.right.size if old_r.right else 0) + 1


                new_r.right = old_r
                new_r.size = old_r.size + (new_r.left.size if new_r.left else 0) + 1


                self.right = new_r

                return self
            else:
                # like example, recalculate size x first then y based on x
                old_r = self.right #x size a+y+1
                new_r = self.right.right #y size b+c+1
                old_r.right = new_r.left 
                old_r.size = (old_r.left.size if old_r.left else 0) + (old_r.right.size if old_r.right else 0) + 1

                new_r.left = old_r
                new_r.size = old_r.size+ (new_r.right.size if new_r.right else 0) + 1

                self.right = new_r

                return self

        elif child_side == "L" and self.left:
            if direction == "R":

                old_l = self.left 
                new_l = self.left.left 
                old_l.left = new_l.right 
                old_l.size = (old_l.left.size if old_l.left else 0) + (old_l.right.size if old_l.right else 0) + 1

                new_l.right = old_l
                new_l.size = old_l.size + (new_l.left.size if new_l.left else 0) + 1

                self.left = new_l
                return self
            else:
                old_l = self.left
                new_l = self.left.right
                old_l.right = new_l.left
                old_l.size = (old_l.left.size if old_l.left else 0) + (old_l.right.size if old_l.right else 0) + 1

                new_l.left = old_l
                new_l.size = old_l.size+ (new_l.right.size if new_l.right else 0) + 1
                self.left = new_l

                return self
                # self.calculate_sizes()
                return self
        return None
        

    def print_bst(self):
        if self.left is not None:
            self.left.print_bst()
        print( self.key),
        if self.right is not None:
            self.right.print_bst()
        return self