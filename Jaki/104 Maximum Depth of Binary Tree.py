# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, node: Optional[TreeNode]) -> int:
        res=1
        if node==None:
            return 0
        else:
            left_max = self.maxDepth(node.left)  
            right_max = self.maxDepth(node.right)
            res+=max(left_max,right_max)
        return res