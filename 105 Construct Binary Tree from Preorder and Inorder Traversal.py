# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder == [] or inorder == []:
            return None
        
        rootVal = preorder[0]
        for i in range(len(inorder)):
            if inorder[i] == rootVal:
                rootIndex = i
        
        inorderLeft = inorder[0:rootIndex]
        lengthLeft = len(inorderLeft)
        preorderLeft = preorder[1:1+lengthLeft]
        left = self.buildTree(preorderLeft, inorderLeft)
        
        inorderRight = inorder[rootIndex+1:]
        lengthRight = len(inorderRight)
        preorderRight = preorder[1+lengthLeft:]
        right = self.buildTree(preorderRight, inorderRight)
        
        #print(rootVal)
        #print(rootIndex)
        #print(preorderLeft)
        #print(inorderLeft)
        #print(preorderRight)
        #print(inorderRight)
        
        root = TreeNode(rootVal, None, None)
        if left != None:
            root.left = left
        if right != None:
            root.right = right
        
        return root
        