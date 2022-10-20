# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def getLCA(node, p, q):
            if not node:
                return None
            if node.val == p or node.val == q:
                return node
            L = getLCA(node.left, p, q)
            R = getLCA(node.right, p, q)
            if L and R:
                return node
            elif L:
                return L
            elif R:
                return R
            else:
                return None
        
        LCA = getLCA(root, startValue, destValue)
        path_start, path_dest = "", ""
        stack = [(LCA, "")]
        while stack: 
            node, path = stack.pop()
            if node.val == startValue: 
                path_start = path 
            if node.val == destValue: 
                path_dest = path
            if node.left: 
                stack.append((node.left, path + "L"))
            if node.right: 
                stack.append((node.right, path + "R"))
                
        return "U"*len(path_start) + path_dest