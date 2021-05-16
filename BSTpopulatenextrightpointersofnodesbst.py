
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return root
        queue = []
        queue.append(root)
        while queue:
            curtmp = []
            nextmp = []
            for node in queue:
                curtmp.append(node)
                if node.left:
                    nextmp.append(node.left)
                if node.right:
                    nextmp.append(node.right)
            queue = nextmp
            for i in range(len(curtmp)-1):
                curtmp[i].next = curtmp[i+1]
            # curtmp[-1].next = None   no necessory
        return root
