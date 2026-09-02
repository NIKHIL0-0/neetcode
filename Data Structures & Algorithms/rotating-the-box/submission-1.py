import heapq

class Solution:
    def rotateTheBox(self, boxGrid):
        m = len(boxGrid)
        n = len(boxGrid[0])

        # Step 1: Rotate 90 degrees clockwise
        box = [['.' for _ in range(m)] for _ in range(n)]

        for r in range(m):
            for c in range(n):
                box[c][m - 1 - r] = boxGrid[r][c]

        # Step 2: Gravity using max heap
        for c in range(m):

            max_heap = []

            # bottom -> top
            for r in range(n - 1, -1, -1):

                # Empty space
                if box[r][c] == '.':
                    heapq.heappush(max_heap, -r)

                # Obstacle
                elif box[r][c] == '*':
                    max_heap.clear()

                # Stone
                elif box[r][c] == '#':

                    # No empty space below
                    if not max_heap:
                        continue

                    # Get lowest empty position
                    empty = -heapq.heappop(max_heap)

                    # Move stone
                    box[empty][c] = '#'
                    box[r][c] = '.'

                    # Old position is now empty
                    heapq.heappush(max_heap, -r)

        return box