# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def rec(node,nod):
            if not node and not nod:
                return True
            elif not node or not nod:
                return False
            if node.val!=nod.val:
                return False
            return rec(node.left,nod.left) and rec(node.right,nod.right)
        return rec(p,q)

        