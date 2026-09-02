class Solution:
    def rotateTheBox(self, boxGrid):
        m = len(boxGrid)
        n = len(boxGrid[0])

        # rotate 90 degrees clockwise
        rotated = [['.' for _ in range(m)] for _ in range(n)]

        for r in range(m):
            for c in range(n):
                rotated[c][m - 1 - r] = boxGrid[r][c]

        # apply gravity column by column
        for c in range(m):
            empty = n - 1

            for r in range(n - 1, -1, -1):

                if rotated[r][c] == '*':
                    empty = r - 1

                elif rotated[r][c] == '#':
                    rotated[r][c] = '.'
                    rotated[empty][c] = '#'
                    empty -= 1

        return rotated