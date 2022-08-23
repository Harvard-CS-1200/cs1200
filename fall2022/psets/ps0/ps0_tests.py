from ps0 import BinaryTree,BTvertex,calculate_sizes,find_vertex

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

# Returns true if removing `v` from the tree rooted at `root`
# ... would result in disjoint trees that all have at most n/2 vertices
def validate_found_vert(root, v):
    threshold = root.size / 2
    t1 = v.left.size if v.left else 0
    t2 = v.right.size if v.right else 0
    t3 = root.size - v.size
    return max([t1, t2, t3]) <= threshold

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

    tests_c = [
        # Format: input

        # Basic tests
        gen_tree(3).root,
        gen_tree(4).root,
        gen_tree(5).root,
        gen_tree(8).root,
        gen_tree(8).root.right,
        # Tests unbalanced tree
        remove_branch(gen_tree(2), 1).root,
        remove_branch(gen_tree(3), 1).root,
        remove_branch(gen_tree(8), 1).root,
        remove_branch(gen_tree(8), 1).root,
    ]
    
    print()
    print("Problem 1c Tests:")
    for i,test in enumerate(tests_c):
        calculate_sizes(test)
        result = find_vertex(test)
        print("Test " + str(i + 1) + ": ", f"{bcolors.OKGREEN}Passed{bcolors.ENDC}" if validate_found_vert(test, result) else f"{bcolors.FAIL}Failed{bcolors.ENDC}")

if __name__ == "__main__":
    test()