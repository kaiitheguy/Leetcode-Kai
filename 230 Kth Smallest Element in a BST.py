# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.arr = []
        self.dfs(root)
        return self.arr[k-1]
    
    def dfs(self, node):
        if node.left != None:
            self.dfs(node.left)
        self.arr.append(node.val)
        if node.right != None:
            self.dfs(node.right)