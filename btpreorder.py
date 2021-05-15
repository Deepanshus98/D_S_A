#non recursion
class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        result=[]
        stack=[]
        stack.append(root)
        while stack:
            tmp=stack.pop()
            result.append(tmp.val)
            if tmp.right:
                stack.append(tmp.right)
            if tmp.left:
                stack.append(tmp.left)
        return result;
#with recursion
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #recursive writing
        result=[]
        def pre(root,result):
            if root==None:
                return None
            result.append(root.val)
            pre(root.left,result)
            pre(root.right,result)
        pre(root,result)
        return result
