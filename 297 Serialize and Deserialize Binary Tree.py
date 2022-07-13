# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.res = ""
        self.dfs(root)
        return self.res
        
    def dfs(self, node):
        if node == None:
            return
        self.res += str(node.val) + ","
        if node.left != None:
            self.dfs(node.left)
        else:
            self.res += "None,"
        if node.right != None:
            self.dfs(node.right)
        else:
            self.res += "None,"

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.deres = []
        return self.deserializeHelper(data.split(",")[:-1])
        
    def deserializeHelper(self, data):
        if len(data) == 0:
            return 
        val = data.pop(0)
        if val == "None":
            return None
        root = TreeNode(val)
        left = self.deserializeHelper(data)
        right = self.deserializeHelper(data)
        root.left = left
        root.right = right
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))