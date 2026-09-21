# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        from collections import deque
        q=deque()
        q.append(root)
        if not root:
            return []
        while q:
            temp=[]
            for i in range (len(q)):
                node=q.popleft()
                if node:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                    temp.append(node.val)
            res.append(temp)
        return res
        