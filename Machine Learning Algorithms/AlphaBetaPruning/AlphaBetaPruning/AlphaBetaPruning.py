from tkinter.tix import Tree

class Treenode:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children is not None else []
        self.isMaximizing = True

def AlphaBeta(node, depth, isMaximizing,alpha,beta):
    if depth == 0 or not node.children:
        return node.value
    if isMaximizing:
        max_eval = -float('inf')
        for child in node.children:
            eval = AlphaBeta(child, depth + 1, False,alpha,beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, max_eval)
            if(beta<=alpha):
                break
        return max_eval
    else:
        min_eval = float('inf')
        for child in node.children:
            eval = AlphaBeta(child, depth + 1, False,alpha,beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, min_eval)
            if(beta<=alpha):
                break
        return min_eval

root = Treenode(1)
node1 = Treenode(3)
node2 = Treenode(-4)
node3 = Treenode(5)
node4 = Treenode(-5)
node5 = Treenode(9)

root.children = [node1, node2,node3,node4,node5]

best_value = AlphaBeta(root,depth=4,isMaximizing=True,alpha=-float('inf'),beta=float('inf'))
print('We are going to apply alpha beta pruning on: ')
for i in root.children:
    print(i.value)
print('Best Value: '+str(best_value))

