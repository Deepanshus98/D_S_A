class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = self.bfs(root)
        res = [res[i] if i%2 == 0 else res[i][::-1] for i in range(len(res))]
        return res
        
    def bfs(self, root):
        res = []
        if not root:
            return res
        q = [root]
        while q:
            res.append([node.val for node in q])
            q = [kid for node in q for kid in (node.left, node.right) if kid]
            
        return res
