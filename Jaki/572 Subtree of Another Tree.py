# https://leetcode.com/problems/subtree-of-another-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root.val == subRoot.val:
            res = self.isSameTree(root,subRoot)
            if res==True:
                return True
        result_left = False
        result_right = False
        if root.left!=None:
            result_left = self.isSubtree(root.left, subRoot)
        if root.right!=None:
            result_right = self.isSubtree(root.right, subRoot)
        if result_left==True or result_right == True:
            return True
        else:
            return False

    
    def isSameTree(self, p, q):
        if p!=None and q!=None:
            if p.val==q.val and self.isSameTree(p.left,q.left)==True and self.isSameTree(p.right,q.right)==True:
                return True
            else:
                return False
        elif (p!=None and q==None) or (q!=None and p==None):
            return False
        else:
            return True
        