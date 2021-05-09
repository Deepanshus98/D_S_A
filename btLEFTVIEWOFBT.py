# A class to store a binary tree node
class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
 
 
# Recursive function to print the left view of a given binary tree
def leftView(root, level=1, last_level=0):
 
    # base case: empty tree
    if root is None:
        return last_level
 
    # if the current node is the first node of the current level
    if last_level < level:
 
        # print the node's data
        print(root.key, end=' ')
 
        # update the last level to the current level
        last_level = level
 
    # recur for the left and right subtree by increasing the level by 1
    last_level = leftView(root.left, level + 1, last_level)
    last_level = leftView(root.right, level + 1, last_level)
 
    return last_level
 
 
if __name__ == '__main__':
 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
 
    leftView(root)
 
