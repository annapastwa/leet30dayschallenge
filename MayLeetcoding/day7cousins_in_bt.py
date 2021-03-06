# Cousins in Binary Tree
# In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
# Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
# We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
# Return true if and only if the nodes corresponding to the values x and y are cousins.
# Note:
# The number of nodes in the tree will be between 2 and 100.
# Each node has a unique integer value from 1 to 100.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """

        def dfs(node, parent, depth):
            if not node or len(results) == 2:
                return
            else:
                if node.val == x or node.val == y:
                    results.append((parent, depth))
                dfs(node.left, node, depth + 1)
                dfs(node.right, node, depth + 1)

        results = []
        dfs(root, None, 0)

        return results[0][0] != results[1][0] and results[0][1] == results[1][1]


foo = Solution()
print(foo.isCousins(3, 4, 5))
