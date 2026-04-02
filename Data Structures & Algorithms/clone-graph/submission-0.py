from collections import deque

class Solution:
    def cloneGraph(self, node):
        if not node:
            return None

        oldToNew = {}
        oldToNew[node] = Node(node.val)

        q = deque([node])

        while q:
            cur = q.popleft()

            for nei in cur.neighbors:
                if nei not in oldToNew:
                    oldToNew[nei] = Node(nei.val)
                    q.append(nei)

                oldToNew[cur].neighbors.append(oldToNew[nei])

        return oldToNew[node]