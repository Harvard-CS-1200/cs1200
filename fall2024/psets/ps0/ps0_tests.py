import random 
import time 
from ps0 import BinaryTree , BTvertex, calculate_sizes, FindDescendantOfSize

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Generates a full/balanced binary tree of `height`
def gen_tree(height, counter = {"val": 1}):
    def gen_vertex(height, counter=counter):
        # Counter needs to be an obj to pass ref
        # Counter needs to be a param if modified or it will be local
        def create_tree_node(counter=counter):
            root = BTvertex(counter["val"])
            # increment counter for key
            counter["val"] += 1
            return root
        def gen_tree_inner(height):
            if height == 1:
                return create_tree_node()
            else:
                root = create_tree_node()
                root.left = gen_vertex(height - 1)
                root.left.parent = root
                root.right = gen_vertex(height - 1)
                root.right.parent = root
                return root
        return gen_tree_inner(height)
    return BinaryTree(gen_vertex(height))

# Removes the outmost branch at `depth` and `side`
def remove_branch(T, depth = 1, side="left"):
    def remove_branch_inner(vertex, depth, side):
        if depth == 1:
            setattr(vertex, side, None)
        else:
            remove_branch_inner(getattr(vertex, side), depth - 1, side)
        return vertex
    remove_branch_inner(T.root, depth, side)
    return T


# Generates a binary tree of size n 
def gen_random_tree_w_n(n):
    if n == 0:
        return None
    
    vertices = [BTvertex(i) for i in range(1, n + 1)]
    
    for i in range(1, n):
        parent = vertices[(i - 1) // 2]  # Find the parent based on 0-indexed array
        vertices[i].parent = parent
        
        # Randomly decide to attach the node as the left or right child
        if parent.left is None:
            parent.left = vertices[i]
        elif parent.right is None:
            parent.right = vertices[i]
        else:
            # handle if both subtrees are already occupied, then override one
            if random.choice([True, False]):
                parent.left = vertices[i]
            else:
                parent.right = vertices[i]

    return BinaryTree(vertices[0])

# creates N trees of size >= 2t + 1, validates that FindDescendantOfSize returns
# correct answer for all created trees
def validate_ans_for_t(t, N):
    time_taken = 0 

    for tree_size in range(2 * t + 1, 2 * t + N + 1): 
        root = gen_random_tree_w_n(tree_size).root
        calculate_sizes(root)

        start = time.time()
        w = FindDescendantOfSize(t, root)
        time_taken += time.time() - start

        # make sure vertex has valid key and size satisfies solution
        if w.size < t or w.size > 2 * t and w.key >= 0 and w.key <= tree_size:
            return False, None
        
    return True, time_taken 


def test():
    tests_a = [
        # Format: (input, postprocessing, expected result)

        # Basic Tests
        (gen_tree(1).root, (lambda root: root), 1),
        (gen_tree(2).root, (lambda root: root), 3),
        (gen_tree(3).root, (lambda root: root), 7),
        (gen_tree(8).root, (lambda root: root), 255),
        (gen_tree(3).root.left, (lambda root: root), 3),
        (gen_tree(3).root.left.right, (lambda root: root), 1),
        (gen_tree(3).root.right, (lambda root: root), 3),
        # Test nodes/subtree
        (gen_tree(3).root, (lambda root: root.left), 3),
        (gen_tree(3).root, (lambda root: root.right), 3),
        (gen_tree(3).root, (lambda root: root.right.left), 1),
        (gen_tree(2).root, (lambda root: root.left), 1),
        # Tests unbalanced tree
        (remove_branch(gen_tree(2), 1).root, (lambda root: root), 2),
        (remove_branch(gen_tree(3), 1).root, (lambda root: root), 4),
        (remove_branch(gen_tree(8), 1).root, (lambda root: root), 255 - 127),
    ]
    print("Problem 1a Tests:")
    for i,test in enumerate(tests_a):
        calculate_sizes(test[0])
        result = test[1](test[0])
        score = result and hasattr(result, "size") and result.size == test[2]
        print("Test " + str(i + 1) + ": ", f"{bcolors.OKGREEN}Passed{bcolors.ENDC}" if score else f"{bcolors.FAIL}Failed{bcolors.ENDC}")


    
    total_time = 0 

    tests_c = [
        # Format (t, N) for creating random binary trees of size >= 2 * t + 1 
        # N is the number of trees to create 

        # params 
        (1, 10), 
        (5, 10), 
        (15, 10), 
        (30, 10), 
        (100, 10), 
        (1000, 50)
    ]
    
    print() 
    print("Problem 1c Tests: ")
    for i, test in enumerate(tests_c):
        t, N = test 
        result, time_taken = validate_ans_for_t(t, N)
        total_time += time_taken
        print("Test " + str(i + 1) + ": ", f"{bcolors.OKGREEN}Passed{bcolors.ENDC}" if result else f"{bcolors.FAIL}Failed{bcolors.ENDC}")
    
    print()
    print(f"Solving Time: {total_time} seconds")

if __name__ == "__main__":
    test()