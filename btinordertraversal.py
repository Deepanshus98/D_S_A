#without recursion
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                t= stack.pop(-1)
                res.append(t.val)
                if t.right:
                    root = t.right
        
        return res
#with recursion
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        ret=[]
        if root==None:
            return ret
        ret.extend(self.inorderTraversal(root.left))
        ret.append(root.val)
        ret.extend(self.inorderTraversal(root.right))
        return ret
