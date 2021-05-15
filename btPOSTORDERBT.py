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
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = list()  #Storing the final result
        if root == None:
            return result
        
        stack = list()  # 
        while stack or root:
            if root != None:   
                stack.append(root)
                root = root.right
            else:
                root = stack.pop()
                result.append(root.val)
                root = root.right
               
                root = stack.pop()
                stack.append(root)

        return result
