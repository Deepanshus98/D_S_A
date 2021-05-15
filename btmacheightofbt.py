class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: # recursive border
            return 0
        else:
            l = 1 + self.maxDepth (root.left) # Recursive
            r=1+self.maxDepth(root.right)
            return max(l,r)
