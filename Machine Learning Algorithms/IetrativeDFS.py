class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

def depth_limited_search(node, goal, depth_limit):
    return dls_recursive(node, goal, depth_limit)

def dls_recursive(node, goal, depth_limit):
    if depth_limit == 0 and node.data != goal:
        return None  # Reached depth limit and goal not found at this depth

    if node.data == goal:
        return node  # Goal found

    for child in node.children:
        result = dls_recursive(child, goal, depth_limit - 1)
        if result:
            return result  # Goal found in child's subtree

    return None  # Goal not found in the current subtree

def deepening_depth_first_search(root, goal):
    depth_limit = 0
    while True:
        result = depth_limited_search(root, goal, depth_limit)
        if result:
            print(f"Goal found at depth {depth_limit}")
            return result  # Goal found
        depth_limit += 1

# Example usage:
# Creating a sample tree
root = Node(1)
root.children = [Node(2), Node(3), Node(4)]
root.children[0].children = [Node(5), Node(6)]
root.children[2].children = [Node(7)]

goal_node = deepening_depth_first_search(root, 6)

if not goal_node:
    print("Goal not found.")
