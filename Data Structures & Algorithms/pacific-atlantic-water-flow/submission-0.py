from collections import deque

class Solution:
    def pacificAtlantic(self, heights):
        if not heights:
            return []

        n, m = len(heights), len(heights[0])
        pac, atl = set(), set()

        def bfs(starts, visited):
            q = deque(starts)
            for r, c in starts:
                visited.add((r, c))

            while q:
                r, c = q.popleft()
                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < n and 0 <= nc < m and 
                        (nr, nc) not in visited and 
                        heights[nr][nc] >= heights[r][c]):
                        
                        visited.add((nr, nc))
                        q.append((nr, nc))

        # Pacific (top row + left col)
        pac_starts = [(0, c) for c in range(m)] + [(r, 0) for r in range(n)]
        
        # Atlantic (bottom row + right col)
        atl_starts = [(n-1, c) for c in range(m)] + [(r, m-1) for r in range(n)]

        bfs(pac_starts, pac)
        bfs(atl_starts, atl)

        # intersection
        return list(pac & atl)