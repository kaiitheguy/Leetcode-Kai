# https://leetcode.com/problems/binary-tree-vertical-order-traversal/

from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        order_dict = defaultdict(list)
        queue = [[root, 0]]
        while queue:
            node_list = queue.pop(0)
            node = node_list[0]
            level = node_list[1]
            order_dict[level].append(node.val)
            if node.left != None:
                queue.append([node.left, level-1])
            if node.right != None:
                queue.append([node.right, level+1])
        res = []
        for i in sorted(order_dict.keys()):
            res.append(order_dict[i])
        return res
    
        