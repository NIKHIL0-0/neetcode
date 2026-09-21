class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sametree(p, q):
            if not p and not q:
                return True

            if not p or not q:
                return False

            if p.val != q.val:
                return False

            return sametree(p.left, q.left) and sametree(p.right, q.right)

        def rec(root):
            if not root:
                return False

            if root.val == subRoot.val and sametree(root, subRoot):
                return True

            return rec(root.left) or rec(root.right)

        return rec(root)