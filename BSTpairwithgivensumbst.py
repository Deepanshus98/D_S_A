# A class to store a BST node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
 
# Recursive function to insert a key into a BST
def insert(root, key):
 
    # if the root is None, create a new node and return it
    if root is None:
        return Node(key)
 
    # if the given key is less than the root node, recur for the left subtree
    if key < root.data:
        root.left = insert(root.left, key)
 
    # if the given key is more than the root node, recur for the right subtree
    else:
        root.right = insert(root.right, key)
 
    return root
 
 
# Function to find a pair with a given sum in a BST
def findPair(root, sum, set):
 
    # base case
    if root is None:
        return False
 
    # return true if pair is found in the left subtree; otherwise, continue
    # processing the node
    if findPair(root.left, sum, set):
        return True
 
    # if a pair is formed with the current node, print the pair and return true
    if sum - root.data in set:
        print("Pair found", (sum - root.data, root.data))
        return True
 
    # insert the current node's value into the set
    else:
        set.add(root.data)
 
    # search in the right subtree
    return findPair(root.right, sum, set)
 
 
if __name__ == '__main__':
 
    keys = [15, 10, 20, 8, 12, 16, 25]
 
    root = None
    for key in keys:
        root = insert(root, key)
 
    # find pair with the given sum
    sum = 28
 
    # create an empty set
    s = set()
 
    if not findPair(root, sum, s):
        print("Pair does not exist")
