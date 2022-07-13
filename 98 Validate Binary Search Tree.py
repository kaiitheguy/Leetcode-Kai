# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValidBSTHelper(root, None, None)
    
    def isValidBSTHelper(self, node, left, right):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if node.left != None:
            if node.left.val >= node.val:
                return False
            else:
                if (left != None and node.left.val <= left) or (right != None and node.left.val >= right):
                    return False
                if not self.isValidBSTHelper(node.left, left, node.val):
                    return False
        if node.right != None:
            if node.right.val <= node.val:
                return False
            else:
                if (left != None and node.right.val <= left) or (right != None and node.right.val >= right):
                    return False
                if not self.isValidBSTHelper(node.right, node.val, right):
                    return False
        return True