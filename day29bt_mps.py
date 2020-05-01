# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxPathSum(self, root):
        """
        Given a non-empty binary tree, find the maximum path sum.
        The path must contain at least one node and does not need to go through the root.
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node):
            """
            Returns: max sum of one side path, max sum of path.
            :param node: node
            :return: int
            """
            left = right = 0
            lside = rside = None

            if node.left:
                left, lside = dfs(node.left)
                left = max(left, 0)
            if node.right:
                right, rside = dfs(node.right)
                right = max(right, 0)
            return node.val + max(left, right), max(node.val + left + right, lside, rside)

        if root:
            return dfs(root)[1]
        return 0


tree = [-10, 9, 20, None, None, 15, 7]
