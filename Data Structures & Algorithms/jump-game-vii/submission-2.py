from collections import deque

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)

        q = deque([0])
        visited = [False] * n
        visited[0] = True

        farthest_scanned = 0

        while q:
            curr = q.popleft()

            start = max(curr + minJump, farthest_scanned + 1)
            end = min(curr + maxJump, n - 1)

            for nxt in range(start, end + 1):
                if s[nxt] == '0' and not visited[nxt]:
                    if nxt == n - 1:
                        return True

                    visited[nxt] = True
                    q.append(nxt)

            farthest_scanned = max(farthest_scanned, end)

        return n == 1