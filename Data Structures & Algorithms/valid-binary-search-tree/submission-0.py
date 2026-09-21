class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        from collections import deque

        if not root:
            return True

        q = deque()
        q.append((root, float('-inf'), float('inf')))

        while q:
            node, low, high = q.pop()

            if node.val <= low or node.val >= high:
                return False

            if node.left:
                q.append((node.left, low, node.val))

            if node.right:
                q.append((node.right, node.val, high))

        return True