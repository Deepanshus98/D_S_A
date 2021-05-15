#Construct Binary Tree from Preorder and Inorder Traversal
class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder == [] or inorder ==[]:
            return None
        val = preorder[0]
        index=inorder.index(val)
        root = TreeNode(val)
        root.left = self.buildTree(preorder[1:index+1],inorder[:index])
        root.right = self.buildTree(preorder[index+1:],inorder[index+1:])
        return root
#106. Construct Binary Tree from Inorder and Postorder Traversal
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if postorder==[]:
            return None 
        val=postorder[-1]
        index=inorder.index(val)
        root=TreeNode(val)
        left=self.buildTree(inorder[:index],postorder[:index])
        
        root.right=self.buildTree(inorder[index+1:],postorder[index:-1])
        root.left=left
        
        return root