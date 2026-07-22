class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def depth(node):
            if not node:
                return 0

            return 1 + max(depth(node.left), depth(node.right))

        if not root:
            return True

        left = depth(root.left)
        right = depth(root.right)

        if abs(left - right) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)