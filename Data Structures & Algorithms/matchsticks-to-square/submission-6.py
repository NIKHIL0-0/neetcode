from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_sum = sum(matchsticks)
        
        # If total length isn't divisible by 4, we can't form a square
        if total_sum % 4 != 0:
            return False
            
        target_side = total_sum // 4
        
        # Sort in descending order to optimize the backtracking search
        matchsticks.sort(reverse=True)
        
        # If the longest single matchstick exceeds the target side, it's impossible
        if matchsticks[0] > target_side:
            return False
            
        # Array to track the current length of the 4 square sides
        sides = [0] * 4
        
        def dfs(index: int) -> bool:
            # If all matchsticks are placed successfully, we found a valid square
            if index == len(matchsticks):
                return True
                
            for i in range(4):
                # Try placing the matchstick in side 'i' if it fits
                if sides[i] + matchsticks[index] <= target_side:
                    sides[i] += matchsticks[index]
                    
                    if dfs(index + 1):
                        return True
                        
                    # Backtrack if the placement didn't lead to a solution
                    sides[i] -= matchsticks[index]
                
                # Optimization: Skip trying identical empty sides to avoid duplicate work
                if sides[i] == 0:
                    break
                    
            return False
            
        return dfs(0)
