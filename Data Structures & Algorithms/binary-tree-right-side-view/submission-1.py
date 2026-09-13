# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        from collections import defaultdict,deque
        if not root:
            return []

        q=deque()
        q.append((root,0))
        res=defaultdict(int)
        while q:
            node,lvl=q.popleft()
            res[lvl]=node.val
            if node.left:
                q.append((node.left,lvl+1))
            if node.right:
                q.append((node.right,lvl+1))
        return list(res.values())
            
            
            
        


