from collections import deque

class Solution:
    def shortestBridge(self, grid):
        n = len(grid)
        seen = set()
        q = deque()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # Find first land cell
        found = False
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
                    seen.add((i, j))
                    found = True
                    break
            if found:
                break

        # Find entire first island
        island = deque(q)

        while island:
            i, j = island.popleft()

            for di, dj in directions:
                ni, nj = i + di, j + dj

                if (
                    0 <= ni < n and
                    0 <= nj < n and
                    grid[ni][nj] == 1 and
                    (ni, nj) not in seen
                ):
                    seen.add((ni, nj))
                    island.append((ni, nj))
                    q.append((ni, nj))  # All Island 1 cells become BFS sources

        # Expand outward using multi-source BFS
        steps = 0

        while q:
            for _ in range(len(q)):
                i, j = q.popleft()

                for di, dj in directions:
                    ni, nj = i + di, j + dj

                    if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in seen:

                        # Reached second island
                        if grid[ni][nj] == 1:
                            return steps

                        seen.add((ni, nj))
                        q.append((ni, nj))

            steps += 1