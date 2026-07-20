# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi=0
        def rec(root):
            nonlocal maxi
            if not root:
                return 0
            l=rec(root.left)
            r=rec(root.right)
            maxi=max(maxi,r+l)
            return 1+max(l,r)
        rec(root)
        return maxi

        