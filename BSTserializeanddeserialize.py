#https://www.youtube.com/watch?v=g6Q1cpQvz8A
class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        res = []
        
        def preorder(root):
            if root:
                res.append(str(root.val))
                preorder(root.left)
                preorder(root.right)
        
        preorder(root)
        return " ".join(res)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        data = [int(x) for x in data.split()]
        
        def build(pre, inorder):
            if not pre:
                return None
            
            node = TreeNode(pre[0])
            temp = inorder.index(node.val)
            node.left = build(pre[1: temp + 1], inorder[:temp])
            node.right = build(pre[temp + 1 :], inorder[temp + 1 :])
            
            return node
        
        return build(data, sorted(data))
