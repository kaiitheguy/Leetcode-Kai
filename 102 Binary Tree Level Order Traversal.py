# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        self.orderedDict = collections.OrderedDict()
        self.traversalHelper(root, 0)
        return self.orderedDict.values()
    
    def traversalHelper(self, node, level):
        if level not in self.orderedDict.keys():
            self.orderedDict[level] = []
        self.orderedDict[level].append(node.val)
        if node.left != None:
            self.traversalHelper(node.left, level+1)
        if node.right != None:
            self.traversalHelper(node.right, level+1)
            