# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        diam = self.maxDepth(root.left) + self.maxDepth(root.right)
        return max(diam, max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right)))

    def maxDepth(self, node):
        if node is None:
            return 0

        left = self.maxDepth(node.left)
        right = self.maxDepth(node.right)
        return max(left, right) + 1

# # Alternative
# class Solution(object):
#     def diameterOfBinaryTree(self, root):
#         self.ans = 1
#         def depth(node):
#             if not node: return 0
#             L = depth(node.left)
#             R = depth(node.right)
#             self.ans = max(self.ans, L+R+1)
#             return max(L, R) + 1
#
#         depth(root)
#         return self.ans - 1
