# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def rec(node):
            if not node:
                return None
            if node==p or node==q:
                return node
            left=rec(node.left)
            right=rec(node.right)
            if left and not right:
                return left
            if right and not left:
                return right
            if left and right:
                return node
            # return None
        return rec(root)
        