# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_path = -float("inf")
        self.maxPathSumHelper(root)
        return self.max_path
    
    def maxPathSumHelper(self, node):
        if node == None:
            return 0
        left = max(self.maxPathSumHelper(node.left), 0)
        right = max(self.maxPathSumHelper(node.right), 0)
        if (left + right + node.val) > self.max_path:
            self.max_path = (left + right + node.val)
        return max(node.val + left, node.val + right)