# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p!=None and q!=None:
            if p.val==q.val and self.isSameTree(p.left,q.left)==True and self.isSameTree(p.right,q.right)==True:
                return True
            else:
                return False
        elif (p!=None and q==None) or (q!=None and p==None):
            return False
        else:
            return True
        
        
        
        

    