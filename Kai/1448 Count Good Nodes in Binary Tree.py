# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        
        def goodNodesHelper(node: TreeNode, maxOnPath: int) -> int:
            if not node:
                return
            if node.val >= maxOnPath:
                self.count += 1
            leftNodes = goodNodesHelper(node.left, max(node.val, maxOnPath))
            rightNodes = goodNodesHelper(node.right, max(node.val, maxOnPath))
            
        goodNodesHelper(root, root.val)
        return self.count