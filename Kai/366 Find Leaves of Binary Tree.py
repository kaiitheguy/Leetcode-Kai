# https://leetcode.com/problems/find-leaves-of-binary-tree/

from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_dict = defaultdict(list)
        
        def findLeavesHelper(node):
            if node.left == None and node.right == None:
                level_dict[0].append(node.val)
                return 0
            else:
                if node.left == None:
                    left_level = 0
                else:
                    left_level = findLeavesHelper(node.left)
                if node.right == None:
                    right_level = 0
                else:
                    right_level = findLeavesHelper(node.right)
                level = max(right_level, left_level) + 1
                level_dict[level].append(node.val)
                return level
            
        findLeavesHelper(root)
        return level_dict.values()
            
        
        