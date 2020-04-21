# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution(object):
#     def bstFromPreorder(self, preorder):
#         """
#         :type preorder: List[int]
#         :rtype: TreeNode
#         """
#
#         if len(preorder) == 0:
#             return
#
#         root = TreeNode(preorder[0])
#
#         def insert(val, root):
#             # we insert a single element using this function
#
#             while True:
#                 # Here we check whether root's value is greater than the given value.
#                 # If yes then try to insert it in the left sub-tree.
#                 if root.val > val:
#                     # Here we check if the left child does not exist then we add a left child with value = val and break the loop
#                     if not root.left:
#                         root.left = TreeNode(val)
#                         break
#                     # Since the left child exists we move towards the left.
#                     else:
#                         root = root.left
#                 # This will work similar to the left child.
#                 else:
#                     if not root.right:
#                         root.right = TreeNode(val)
#                         break
#                     else:
#                         root = root.right
#
#         head = root
#         for i in range(1, len(preorder)):
#             # Here we reset the head pointer so we are the top of the tree again.
#             head = root
#             insert(preorder[i], head)
#
#         return head

# Alternative
# Idea is simple.
# First item in preorder list is the root to be considered.
# For next item in preorder list, there are 2 cases to consider:
# If value is less than last item in stack, it is the left child of last item.
# If value is greater than last item in stack, pop it.
# The last popped item will be the parent and the item will be the right child of the parent.

class Solution(object):
    def bstFromPreorder(self, preorder):
        root = TreeNode(preorder[0])
        stack = [root]
        for value in preorder[1:]:
            if value < stack[-1].val:
                stack[-1].left = TreeNode(value)
                stack.append(stack[-1].left)
            else:
                while stack and stack[-1].val < value:
                    last = stack.pop()
                last.right = TreeNode(value)
                stack.append(last.right)
        return root

preorder = [8, 5, 1, 7, 10, 12]
foo = Solution()
print(foo.bstFromPreorder(preorder).val)  # print head


