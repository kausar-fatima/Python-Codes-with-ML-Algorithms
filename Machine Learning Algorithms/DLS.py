#implementing depth limited search
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

    return None  # Goal not found in current subtree

# Example usage:
# Creating a sample tree
root = Node(1)
root.children = [Node(2), Node(3), Node(4)]
root.children[0].children = [Node(5), Node(6)]
root.children[2].children = [Node(7)]

goal_node = depth_limited_search(root, 6, 2)

if goal_node:
    print(f"Goal found: {goal_node.data}")
else:
    print("Goal not found within the depth limit.")
