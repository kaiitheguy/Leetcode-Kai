# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        visited = []
        queue = []
        orders = collections.defaultdict(list)
        
        visited.append(root)
        queue.append([root, 0, 0])
        
        while queue:
            node = queue.pop(0)
            orders[node[2]].append((node[0].val, node[1]))
            
            if node[0].left != None and node[0].left not in visited:
                visited.append(node[0].left)
                queue.append([node[0].left, node[1]+1, node[2]-1])
            
            if node[0].right != None and node[0].right not in visited:
                visited.append(node[0].right)
                queue.append([node[0].right, node[1]+1, node[2]+1])
                    
        return [[i[0] for i in sorted(item[1], key=lambda x: (x[1], x[0]))] 
                for item in sorted(orders.items())]