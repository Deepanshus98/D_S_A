# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
            if root is None:
                return []
            res = []
            stack = [root]
            left = True # True: left->right,  False: right->left
            while stack:
                tmp = []
                tmp_stack=[]
                for _ in range(len(stack)):
                    node = stack.pop()
                    tmp.append(node.val)
                    if left:
                        if node.left: tmp_stack.append(node.left)
                        if node.right: tmp_stack.append(node.right)
                    else:
                        if node.right: tmp_stack.append(node.right)
                        if node.left: tmp_stack.append(node.left)
                res.append(tmp)
                stack = tmp_stack
                left = not left
            return res
