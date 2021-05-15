class Solution:
    def __init__(self):
        self.maxSum = float("-inf")

    def maxPathSum(self, root: TreeNode) -> int:
        def maxdepth(root):
            if not root:
                return 0
            leftsum = max(maxdepth(root.left), 0)
            rightsum = max(maxdepth(root.right), 0)
            sum = leftsum + rightsum + root.val
            self.maxSum = max(sum, self.maxSum)
            return max(leftsum, rightsum) + root.val
        maxdepth(root)
        return self.maxSum
