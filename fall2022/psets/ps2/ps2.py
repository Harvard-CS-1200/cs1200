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
        if left_size < ind and self.right is not None:
            return self.right.select(ind - left_size - 1)
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
        elif self.key > key: 
            if self.left is None:
                self.left = BinarySearchTree(self.debugger)
            self.size += 1
            self.left.insert(key)
        elif self.key < key:
            if self.right is None:
                self.right = BinarySearchTree(self.debugger)
            self.size += 1
            self.right.insert(key)
        # self.calculate_sizes()
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
        if self == None:
            return self
        
        parent_chunk_size = 0
        child_size = 0
        child_child_size = 0

        if direction == 'L' and child_side == 'R':

            if self.right.left:
                parent_chunk_size = self.right.left.size
            if self.right.right:  
                child_size = self.right.right.size
            if self.right.right.left:
                child_child_size = self.right.right.left.size

            keep = self.right
            keep_child_child = self.right.right.left
            self.right = self.right.right
            self.right.size = self.right.size - child_child_size + parent_chunk_size + 1
            
            self.right.left = keep
            self.right.left.right = keep_child_child
            self.right.left.size = self.right.left.size + child_child_size - child_size

        elif direction == 'R' and child_side == 'L':

            if self.left.right:
                parent_chunk_size = self.left.right.size
            if self.left.left:  
                child_size = self.left.left.size
            if self.left.left.right:
                child_child_size = self.left.left.right.size

            keep = self.left
            keep_child_child = self.left.left.right
            self.left = self.left.left
            self.left.size = self.left.size - child_child_size + parent_chunk_size + 1

            self.left.right = keep
            self.left.right.left = keep_child_child
            self.left.right.size = self.left.right.size + child_child_size - child_size

        elif direction == 'L' and child_side == 'L':

            if self.left.left:
                parent_chunk_size = self.left.left.size
            if self.left.right:  
                child_size = self.left.right.size
            if self.left.right.left:
                child_child_size = self.left.right.left.size

            keep = self.left
            keep_child_child = self.left.right.left
            self.left = self.left.right
            self.left.size = self.left.size - child_child_size + parent_chunk_size + 1

            self.left.left = keep
            self.left.left.right = keep_child_child
            self.left.left.size = self.left.left.size + child_child_size - child_side

        elif direction == 'R' and child_side == 'R':

            if self.right.right:
                parent_chunk_size = self.right.right.size
            if self.right.left:  
                child_size = self.right.left.size
            if self.right.left.right:
                child_child_size = self.right.left.right.size

            keep = self.right
            keep_child_child = self.right.left.right
            self.right = self.right.left
            self.right.size = self.right.size - child_child_size + parent_chunk_size + 1

            self.right.right = keep
            self.right.right.left = keep_child_child
            self.right.right.size = self.right.right.size + child_child_size - child_size
        
        return self

    def print_bst(self):
        if self.left is not None:
            self.left.print_bst()
        print( self.key),
        if self.right is not None:
            self.right.print_bst()
        return self