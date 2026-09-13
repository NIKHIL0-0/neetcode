from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Get matrix dimensions
        n = len(board)
        m = len(board[0])
        seen = set()
        
        def dfs(r, c, index):
            # Base Case: Entire word has been successfully matched
            if index == len(word):
                return True
                
            # Boundary check, visited check, and character match check
            if (r < 0 or r >= n or 
                c < 0 or c >= m or 
                (r, c) in seen or 
                board[r][c] != word[index]):
                return False
            
            # Action: Mark the current cell as visited
            seen.add((r, c))
            
            # Explore all 4 directions (Up, Down, Left, Right)
            # If any direction returns True, we found the word
            found = (dfs(r + 1, c, index + 1) or
                     dfs(r - 1, c, index + 1) or
                     dfs(r, c + 1, index + 1) or
                     dfs(r, c - 1, index + 1))
            
            # Backtrack: Remove the cell so other paths can reuse it
            seen.remove((r, c))
            
            return found

        # Traverse every cell in the grid to find a potential starting point
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
                        
        return False
