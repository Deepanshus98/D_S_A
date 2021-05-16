#without recursion
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            if root.left is not None:
                stack.append(root.left)
            if root.right is not None:
                stack.append(root.right)
                
        return output[::-1]
#with recursion

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def helper(root, l):
            if root is None:
                return
            helper(root.left, l)
            helper(root.right, l)
            l.append(root.val)
        l = []
        helper(root, l)
        return l
