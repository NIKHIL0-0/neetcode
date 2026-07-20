# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxi=0
        if root==None:
            return 0
        def rec(rot,val):
            nonlocal maxi
            if not rot:
                return None
            maxi=max(maxi,val)
            rec(rot.left,val+1)
            rec(rot.right,val+1)
        rec(root,1)
        return maxi       