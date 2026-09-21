# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res=0
        from collections import deque
        q=deque()
        q.append((root,root.val))
        if not root:
            return 0
        while q:
            node,maxi=q.pop()
            if node.val>=maxi:
                res+=1
            maxi=max(node.val,maxi)
            if node.left:
                q.append((node.left,maxi))
            if node.right:
                q.append((node.right,maxi))
        return res

            