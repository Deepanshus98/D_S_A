#with recursion
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        res = []
        res += self.postorderTraversal(root.left)
        res += self.postorderTraversal(root.right)
        res.append(root.val)
        return res
#without recursion

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
